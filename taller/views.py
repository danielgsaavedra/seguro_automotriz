from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import timezone
from django.http import JsonResponse
from .forms import ActasForm, InformeDañosForm, CambiarEstadoForm
from dashboard.models import Siniestro, EstadoSiniestro, FormularioActa, TipoActa, Poliza, Taller, Vehiculo, \
    InformeDano, Usuario, Presupuesto
from django.db import connection
import pdfkit
import datetime
from django.http import HttpResponse
from django.db.models import Q


# ACTA RECEPCION


def SaveAllActaRecepcion(request, form, template_name):
    data = dict()
    estado = get_object_or_404(EstadoSiniestro, id=1)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            actas = Siniestro.objects.filter(
                est_siniestro_id_est_siniestro=estado).order_by('id')
            context = {'actas': actas}
            data['actas'] = render_to_string(
                'taller/acta_recepcion/siniestro_recepcion_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


@login_required(login_url='login')
def ActaRecepcionView(request):
    with connection.cursor() as cursor:
        cursor.callproc('SP_ESTADO_GRUAS')
    estado = get_object_or_404(TipoActa, id=1)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    actas = FormularioActa.objects.filter(
        Q(tipo_acta_id_tipo_acta=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'actas': actas}
    return render(request, 'taller/acta_recepcion/acta_recepcion.html', context)


@login_required(login_url='login')
def CreateActaRecepcion(request, id):
    with connection.cursor() as cursor:
        cursor.callproc('SP_ESTADO_GRUAS')
    data = dict()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.TALLER_ID_TALLER, S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) WHERE(S.TALLER_ID_TALLER = T.ID AND S.ID=" + id + ")")
        dato = cursor.fetchall()
        dato = list(dato)
    tipo_acta = get_object_or_404(TipoActa, id=1)
    siniestro_id = get_object_or_404(Siniestro, id=dato[0][1])
    taller_id = get_object_or_404(Taller, id=dato[0][0])

    if request.method == 'POST':
        print(dato[0][1])
        form = ActasForm(request.POST)
        if form.is_valid():
            acta = form.save(commit=False)
            acta.usuario_rut_usuario = request.user
            acta.tipo_acta_id_tipo_acta = tipo_acta
            acta.siniestro_id = siniestro_id
            acta.taller_id_taller = taller_id
            acta.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ActasForm()
    context = {'form': form, 'siniestro_id': siniestro_id}
    data['html_form'] = render_to_string(
        'taller/acta_recepcion/acta_recepcion_create.html', context, request=request)
    return JsonResponse(data)


def actaRecepcionViewPdf(request, pk):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.DESCRIPCION,S.GRUA_PATENTE_GRUA,S.POLIZA_ID_POLIZA,S.ASEGURADO_RUT_ASEGURADO,F.ID,F.FECHA_HORA,F.OBSERVACIONES,V.PATENTE_VEHICULO,V.MODELO,V.ANIO,V.NRO_MOTOR,A.PRIMER_NOMBRE,A.PRIMER_APELLIDO,A.CORREO,A.TELEFONO,T.NOMBRE,T.RAZON_SOCIAL,T.TELEFONO,T.CORREO,M.NOMBRE,S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_FORMULARIOACTA F ON (S.ID=F.SINIESTRO_ID) JOIN DASHBOARD_VEHICULO V ON (S.ASEGURADO_RUT_ASEGURADO=V.ASEGURADO_RUT_ASEGURADO) JOIN DASHBOARD_ASEGURADO A ON (S.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO) JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_MARCA M ON (V.MARCA_ID_MARCA=M.ID) WHERE(f.tipo_acta_id_tipo_acta=1 AND S.ID=" + pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/acta_recepcion/pdf/acta_pdf.html', {'dato': dato})


def actaRecepcionPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '0.7in',
        'margin-bottom': '0.5in',
        'margin-left': '0.7in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/taller/actaRecepcionViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ActaRecepcion.pdf" '
    return response


@login_required(login_url='login')
def SiniestrosRecepcionView(request):
    estado = get_object_or_404(EstadoSiniestro, id=1)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    with connection.cursor() as cursor:
        cursor.callproc('SP_CAMBIAR_GARANTIA')
    siniestros = Siniestro.objects.filter(
        Q(est_siniestro_id_est_siniestro=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/acta_recepcion/siniestro_recepcion.html', context)


# ACTA RETIRO


def SaveAllActaRetiro(request, form, template_name):
    data = dict()
    estado = get_object_or_404(EstadoSiniestro, id=6)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            actas = Siniestro.objects.filter(
                est_siniestro_id_est_siniestro=estado).order_by('id')
            context = {'actas': actas}
            data['actas'] = render_to_string(
                'taller/acta_retiro/siniestro_retiro_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


@login_required(login_url='login')
def ActaRetiroView(request):
    estado = get_object_or_404(TipoActa, id=3)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    actas = FormularioActa.objects.filter(
        Q(tipo_acta_id_tipo_acta=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'actas': actas}
    return render(request, 'taller/acta_retiro/acta_retiro.html', context)


@login_required(login_url='login')
def CreateActaRetiro(request, id):
    data = dict()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.TALLER_ID_TALLER, S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) WHERE(S.TALLER_ID_TALLER = T.ID AND S.ID=" + id + ")")
        dato = cursor.fetchall()
        dato = list(dato)
    tipo_acta = get_object_or_404(TipoActa, id=3)
    siniestro_id = get_object_or_404(Siniestro, id=dato[0][1])
    taller_id = get_object_or_404(Taller, id=dato[0][0])

    if request.method == 'POST':
        print(dato[0][1])
        form = ActasForm(request.POST)
        if form.is_valid():
            acta = form.save(commit=False)
            acta.usuario_rut_usuario = request.user
            acta.tipo_acta_id_tipo_acta = tipo_acta
            acta.siniestro_id = siniestro_id
            acta.taller_id_taller = taller_id
            acta.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ActasForm()
    context = {'form': form, 'siniestro_id': siniestro_id}
    data['html_form'] = render_to_string(
        'taller/acta_retiro/acta_retiro_create.html', context, request=request)
    return JsonResponse(data)


def actaRetiroViewPdf(request, pk):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.DESCRIPCION,S.GRUA_PATENTE_GRUA,S.POLIZA_ID_POLIZA,S.ASEGURADO_RUT_ASEGURADO,F.ID,F.FECHA_HORA,F.OBSERVACIONES,V.PATENTE_VEHICULO,V.MODELO,V.ANIO,V.NRO_MOTOR,A.PRIMER_NOMBRE,A.PRIMER_APELLIDO,A.CORREO,A.TELEFONO,T.NOMBRE,T.RAZON_SOCIAL,T.TELEFONO,T.CORREO,M.NOMBRE,S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_FORMULARIOACTA F ON (S.ID=F.SINIESTRO_ID) JOIN DASHBOARD_VEHICULO V ON (S.ASEGURADO_RUT_ASEGURADO=V.ASEGURADO_RUT_ASEGURADO) JOIN DASHBOARD_ASEGURADO A ON (S.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO) JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_MARCA M ON (V.MARCA_ID_MARCA=M.ID) WHERE(f.tipo_acta_id_tipo_acta=3 AND S.ID=" + pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/acta_retiro/pdf/acta_pdf_retiro.html', {'dato': dato})


def actaRetiroPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '0.7in',
        'margin-bottom': '0.5in',
        'margin-left': '0.7in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/taller/actaRetiroViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ActaRetiro.pdf" '
    return response


@login_required(login_url='login')
def SiniestrosRetiroView(request):
    estado = get_object_or_404(EstadoSiniestro, id=6)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    with connection.cursor() as cursor:
        cursor.callproc('SP_ACTIVAR_ESTADO_PENDIENTE')
    with connection.cursor() as cursor:
        cursor.callproc('SP_CAMBIAR_GARANTIA')
    siniestros = Siniestro.objects.filter(
        Q(est_siniestro_id_est_siniestro=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/acta_retiro/siniestro_retiro.html', context)


# ACTA RECHAZO


@login_required(login_url='login')
def ActaRechazoView(request):
    estado = get_object_or_404(TipoActa, id=2)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    actas = FormularioActa.objects.filter(
        Q(tipo_acta_id_tipo_acta=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'actas': actas}
    return render(request, 'taller/acta_retiro/acta_rechazo.html', context)


@login_required(login_url='login')
def CreateActaRechazo(request, id):
    data = dict()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.TALLER_ID_TALLER, S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) WHERE(S.TALLER_ID_TALLER = T.ID AND S.ID=" + id + ")")
        dato = cursor.fetchall()
        dato = list(dato)
    tipo_acta = get_object_or_404(TipoActa, id=2)
    siniestro_id = get_object_or_404(Siniestro, id=dato[0][1])
    taller_id = get_object_or_404(Taller, id=dato[0][0])

    if request.method == 'POST':
        print(dato[0][1])
        form = ActasForm(request.POST)
        if form.is_valid():
            acta = form.save(commit=False)
            acta.usuario_rut_usuario = request.user
            acta.tipo_acta_id_tipo_acta = tipo_acta
            acta.siniestro_id = siniestro_id
            acta.taller_id_taller = taller_id
            acta.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ActasForm()
    context = {'form': form, 'siniestro_id': siniestro_id}
    data['html_form'] = render_to_string(
        'taller/acta_retiro/acta_rechazo_create.html', context, request=request)
    return JsonResponse(data)


def actaRechazoViewPdf(request, pk):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.DESCRIPCION,S.GRUA_PATENTE_GRUA,S.POLIZA_ID_POLIZA,S.ASEGURADO_RUT_ASEGURADO,F.ID,F.FECHA_HORA,F.OBSERVACIONES,V.PATENTE_VEHICULO,V.MODELO,V.ANIO,V.NRO_MOTOR,A.PRIMER_NOMBRE,A.PRIMER_APELLIDO,A.CORREO,A.TELEFONO,T.NOMBRE,T.RAZON_SOCIAL,T.TELEFONO,T.CORREO,M.NOMBRE,S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_FORMULARIOACTA F ON (S.ID=F.SINIESTRO_ID) JOIN DASHBOARD_VEHICULO V ON (S.ASEGURADO_RUT_ASEGURADO=V.ASEGURADO_RUT_ASEGURADO) JOIN DASHBOARD_ASEGURADO A ON (S.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO) JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_MARCA M ON (V.MARCA_ID_MARCA=M.ID) WHERE(f.tipo_acta_id_tipo_acta=2 AND S.ID=" + pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/acta_retiro/pdf/acta_pdf_rechazo.html', {'dato': dato})


def actaRechazoPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '0.7in',
        'margin-bottom': '0.5in',
        'margin-left': '0.7in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/taller/actaRechazoViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ActaRechazo.pdf" '
    return response


# INFORME DE DAÑOS


def SaveAllInformeDanos(request, form, template_name):
    data = dict()
    estado = get_object_or_404(EstadoSiniestro, id=2)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            actas = Siniestro.objects.filter(
                est_siniestro_id_est_siniestro=estado).order_by('id')
            context = {'actas': actas}
            data['actas'] = render_to_string(
                'taller/informe_daños/informe_daños_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


@login_required(login_url='login')
def CreateInformeDaños(request, id):
    data = dict()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.TALLER_ID_TALLER, S.ID, V.PATENTE_VEHICULO FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_VEHICULO V ON (V.ASEGURADO_RUT_ASEGURADO = S.ASEGURADO_RUT_ASEGURADO) WHERE(S.TALLER_ID_TALLER = T.ID AND S.ID=" + id + ")")
        dato = cursor.fetchall()
        dato = list(dato)
    siniestro_id = get_object_or_404(Siniestro, id=dato[0][1])
    taller_id = get_object_or_404(Taller, id=dato[0][0])
    patente_vehiculo = get_object_or_404(Vehiculo, patente_vehiculo=dato[0][2])

    if request.method == 'POST':
        print(dato[0][1])
        form = InformeDañosForm(request.POST)
        if form.is_valid():
            info_dano = form.save(commit=False)
            info_dano.usuario_rut_usuario = request.user
            info_dano.siniestro_id = siniestro_id
            info_dano.taller_id_taller = taller_id
            info_dano.vehiculo_patente_vehiculo = patente_vehiculo
            info_dano.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = InformeDañosForm()
    context = {'form': form, 'siniestro_id': siniestro_id}
    data['html_form'] = render_to_string(
        'taller/informe_daños/informe_daños_create.html', context, request=request)
    return JsonResponse(data)


@login_required(login_url='login')
def SiniestrosInformeDañosView(request):
    estado = get_object_or_404(EstadoSiniestro, id=2)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    siniestros = Siniestro.objects.filter(
        Q(est_siniestro_id_est_siniestro=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/informe_daños/informe_daños.html', context)


@login_required(login_url='login')
def InformeDanosView(request):
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    info_danos = InformeDano.objects.filter(taller_id_taller=taller)
    context = {'info_danos': info_danos}
    return render(request, 'taller/informe_daños/informe_daños_view.html', context)


@login_required(login_url='login')
def InformeDanosDetail(request, id):
    data = dict()
    info = get_object_or_404(InformeDano, id=id)
    context = {'info': info}
    data['html_form'] = render_to_string(
        'taller/informe_daños/informe_daños_detail.html', context, request=request)
    return JsonResponse(data)


# SINIESTROS INSPECCIONADOS

@login_required(login_url='login')
def SiniestrosInpeccionadosView(request):
    estado = get_object_or_404(EstadoSiniestro, id=3)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    siniestros = Siniestro.objects.filter(
        Q(est_siniestro_id_est_siniestro=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/siniestros/siniestros_inspeccionados_view.html', context)


@login_required(login_url='login')
def CambiarEstadoEnReparacion(request, id):
    data = dict()
    siniestro = get_object_or_404(Siniestro, id=id)
    estado = get_object_or_404(EstadoSiniestro, id=3)
    estado_new = get_object_or_404(EstadoSiniestro, id=4)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    if request.method == 'POST':
        form = CambiarEstadoForm(request.POST, instance=siniestro)
        if form.is_valid():
            siniestro = form.save(commit=False)
            siniestro.est_siniestro_id_est_siniestro = estado_new
            siniestro.save()
            data['form_is_valid'] = True
            siniestros = Siniestro.objects.filter(
                Q(est_siniestro_id_est_siniestro=estado) &
                Q(taller_id_taller=taller)
            ).order_by('id')
            context = {'siniestros': siniestros}
            data['siniestros'] = render_to_string(
                'taller/siniestros/siniestros_inspeccionados_view_2.html', context)
    else:
        form = CambiarEstadoForm(instance=siniestro)
        data['form_is_valid'] = False
        context = {'siniestro': siniestro, 'form': form}
        data['html_form'] = render_to_string(
            'taller/siniestros/cambiar_estado_reparacion.html', context, request=request)
    return JsonResponse(data)


# SINIESTROS ENREPARACION
@login_required(login_url='login')
def SiniestrosEnReparacionView(request):
    estado = get_object_or_404(EstadoSiniestro, id=4)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    siniestros = Siniestro.objects.filter(
        Q(est_siniestro_id_est_siniestro=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/siniestros/siniestros_enreparacion_view.html', context)


@login_required(login_url='login')
def CambiarEstadoReparado(request, id):
    data = dict()
    siniestro = get_object_or_404(Siniestro, id=id)
    estado = get_object_or_404(EstadoSiniestro, id=4)
    estado_new = get_object_or_404(EstadoSiniestro, id=6)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    print(siniestro.asegurado_rut_asegurado.correo)
    if request.method == 'POST':
        form = CambiarEstadoForm(request.POST, instance=siniestro)
        if form.is_valid():
            siniestro = form.save(commit=False)
            siniestro.est_siniestro_id_est_siniestro = estado_new
            siniestro.save()
            data['form_is_valid'] = True
            correo = EmailMessage(
                'SEGUROS VIRGOLINI: VEHÍCULO REPARADO',
                'Estimado/a {} {}.\n\nSu vehículo gestionado en el siniestro N°{} se encuentra disponible para retiro.\n\nFavor comunicarse con taller {} al teléfeno +56{} para coordinar retiro.\n\nSaludos cordiales.'.format(
                    siniestro.asegurado_rut_asegurado.primer_nombre, siniestro.asegurado_rut_asegurado.primer_apellido,
                    siniestro.id, siniestro.taller_id_taller.nombre, siniestro.taller_id_taller.telefono),
                'no-contestar@hotmail.com',
                [siniestro.asegurado_rut_asegurado.correo],
                reply_to=['lobos.joaquin@hotmail.com']
            )
            correo.send()
            siniestros = Siniestro.objects.filter(
                Q(est_siniestro_id_est_siniestro=estado) &
                Q(taller_id_taller=taller)
            ).order_by('id')
            context = {'siniestros': siniestros}
            data['siniestros'] = render_to_string(
                'taller/siniestros/siniestros_enreparacion_view_2.html', context)
    else:
        form = CambiarEstadoForm(instance=siniestro)
        data['form_is_valid'] = False
        context = {'siniestro': siniestro, 'form': form}
        data['html_form'] = render_to_string(
            'taller/siniestros/cambiar_estado_reparado.html', context, request=request)
    return JsonResponse(data)


@login_required(login_url='login')
def SiniestrosRechazadoView(request):
    estado = get_object_or_404(EstadoSiniestro, id=5)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    siniestros = Siniestro.objects.filter(
        Q(est_siniestro_id_est_siniestro=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/siniestros/siniestros_rechazado_view.html', context)


@login_required(login_url='login')
def SiniestrosPendienteView(request):
    estado = get_object_or_404(EstadoSiniestro, id=8)
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    siniestros = Siniestro.objects.filter(
        Q(est_siniestro_id_est_siniestro=estado) &
        Q(taller_id_taller=taller)
    ).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/siniestros/siniestros_pendiente_view.html', context)


def informeDanoViewPdf(request, pk):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT I.ID,I.FECHA_HORA,I.SINIESTRO_ID,I.OBSERVACIONES,I.VEHICULO_PATENTE_VEHICULO,I.PERDIDA_TOTAL,S.NOMBRE,T.NOMBRE,T.DESCRIPCION,X.NOMBRE,X.RAZON_SOCIAL,X.TELEFONO,X.CORREO FROM DASHBOARD_INFORMEDANO I JOIN DASHBOARD_SEVERIDADDANO S ON (S.ID=I.SEVERIDAD_DANO_ID_SEVE_DANO) JOIN DASHBOARD_TIPODANO T ON (T.ID=I.TIPO_DANO_ID_TIPO_DANO) JOIN DASHBOARD_TALLER X ON(X.ID=I.TALLER_ID_TALLER) WHERE(I.ID=" + pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/informe_daños/pdf/informe_dano_pdf.html', {'dato': dato})


def informeDanoPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '0.7in',
        'margin-bottom': '0.5in',
        'margin-left': '0.7in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/talle/rinformeDanoViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="informeDanoPdf.pdf" '
    return response


def crearPresupuesto(request, pk):
    with connection.cursor() as cursor:
        cursor.callproc('SP_CREAR_PRESUPUESTO', [pk])
    return render(request, 'taller/informe_daños/informe_daños_view.html')


@login_required(login_url='login')
def PresupuestoView(request):
    taller = get_object_or_404(Taller, id=request.user.taller_id_taller.id)
    presupuestos = Presupuesto.objects.filter(taller_id_taller=taller).order_by('id')
    context = {'presupuestos': presupuestos}
    return render(request, 'taller/presupuestos/presupuestos_view.html', context)


def PresupuestoViewPdf(request, pk):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT P.ID,P.FECHA_HORA,P.VALOR_TOTAL,P.ESTADO_ID_EST_PRESUPUESTO,I.ID,I.SINIESTRO_ID,I.VEHICULO_PATENTE_VEHICULO,I.OBSERVACIONES,T.NOMBRE,D.NOMBRE,D.DESCRIPCION,D.VALOR,D.MANO_OBRA,S.NOMBRE,S.VALOR FROM DASHBOARD_PRESUPUESTO P JOIN DASHBOARD_INFORMEDANO I ON (I.ID=P.INFORME_DANO_ID_INFO_DANO) JOIN DASHBOARD_TALLER T ON (T.ID=I.TALLER_ID_TALLER) JOIN DASHBOARD_TIPODANO D ON (D.ID=I.TIPO_DANO_ID_TIPO_DANO) JOIN DASHBOARD_SEVERIDADDANO S ON (S.ID=I.SEVERIDAD_DANO_ID_SEVE_DANO) WHERE (P.ID=" + pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/presupuestos/pdf/presupuesto_pdf.html', {'dato': dato})


def PresupuestoPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '0.7in',
        'margin-bottom': '0.5in',
        'margin-left': '0.7in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/taller/PresupuestoViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Presupuesto.pdf" '
    return response
