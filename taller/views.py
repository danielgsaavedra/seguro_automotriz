from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import timezone
from django.http import JsonResponse
from .forms import ActasForm
from dashboard.models import Siniestro, EstadoSiniestro, FormularioActa, TipoActa, Poliza, Taller
from django.db import connection
import pdfkit
from django.http import HttpResponse

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
    estado = get_object_or_404(TipoActa, id=1)
    actas = FormularioActa.objects.filter(
        tipo_acta_id_tipo_acta=estado).order_by('id')
    context = {'actas': actas}
    return render(request, 'taller/acta_recepcion/acta_recepcion.html', context)

@login_required(login_url='login')
def CreateActaRecepcion(request, id):
    data = dict()
    with connection.cursor() as cursor:
        cursor.execute("SELECT S.TALLER_ID_TALLER, S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) WHERE(S.TALLER_ID_TALLER = T.ID AND S.ID=" + id + ")")
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
        cursor.execute("SELECT S.DESCRIPCION,S.GRUA_PATENTE_GRUA,S.POLIZA_ID_POLIZA,S.ASEGURADO_RUT_ASEGURADO,F.ID,F.FECHA_HORA,F.OBSERVACIONES,V.PATENTE_VEHICULO,V.MODELO,V.ANIO,V.NRO_MOTOR,A.PRIMER_NOMBRE,A.PRIMER_APELLIDO,A.CORREO,A.TELEFONO,T.NOMBRE,T.RAZON_SOCIAL,T.TELEFONO,T.CORREO,M.NOMBRE,S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_FORMULARIOACTA F ON (S.ID=F.SINIESTRO_ID) JOIN DASHBOARD_VEHICULO V ON (S.ASEGURADO_RUT_ASEGURADO=V.ASEGURADO_RUT_ASEGURADO) JOIN DASHBOARD_ASEGURADO A ON (S.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO) JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_MARCA M ON (V.MARCA_ID_MARCA=M.ID) WHERE(f.tipo_acta_id_tipo_acta=1 AND S.ID="+pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/acta_recepcion/pdf/acta_pdf.html', {'dato': dato})

def actaRecepcionPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '1in',
        'margin-bottom': '0.5in',
        'margin-left': '1in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/actaRecepcionViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ActaRecepcion.pdf" '
    return response

@login_required(login_url='login')
def SiniestrosRecepcionView(request):
    estado = get_object_or_404(EstadoSiniestro, id=1)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
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
    actas = FormularioActa.objects.filter(
        tipo_acta_id_tipo_acta=estado).order_by('id')
    context = {'actas': actas}
    return render(request, 'taller/acta_retiro/acta_retiro.html', context)

@login_required(login_url='login')
def CreateActaRetiro(request, id):
    data = dict()
    with connection.cursor() as cursor:
        cursor.execute("SELECT S.TALLER_ID_TALLER, S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) WHERE(S.TALLER_ID_TALLER = T.ID AND S.ID=" + id + ")")
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
        cursor.execute("SELECT S.DESCRIPCION,S.GRUA_PATENTE_GRUA,S.POLIZA_ID_POLIZA,S.ASEGURADO_RUT_ASEGURADO,F.ID,F.FECHA_HORA,F.OBSERVACIONES,V.PATENTE_VEHICULO,V.MODELO,V.ANIO,V.NRO_MOTOR,A.PRIMER_NOMBRE,A.PRIMER_APELLIDO,A.CORREO,A.TELEFONO,T.NOMBRE,T.RAZON_SOCIAL,T.TELEFONO,T.CORREO,M.NOMBRE,S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_FORMULARIOACTA F ON (S.ID=F.SINIESTRO_ID) JOIN DASHBOARD_VEHICULO V ON (S.ASEGURADO_RUT_ASEGURADO=V.ASEGURADO_RUT_ASEGURADO) JOIN DASHBOARD_ASEGURADO A ON (S.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO) JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_MARCA M ON (V.MARCA_ID_MARCA=M.ID) WHERE(f.tipo_acta_id_tipo_acta=1 AND S.ID="+pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/acta_retiro/pdf/acta_pdf_retiro.html', {'dato': dato})

def actaRetiroPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '1in',
        'margin-bottom': '0.5in',
        'margin-left': '1in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/actaRetiroViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ActaRetiro.pdf" '
    return response

@login_required(login_url='login')
def SiniestrosRetiroView(request):
    estado = get_object_or_404(EstadoSiniestro, id=6)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/acta_retiro/siniestro_retiro.html', context)


# ACTA RECHAZO


@login_required(login_url='login')
def ActaRechazoView(request):
    estado = get_object_or_404(TipoActa, id=2)
    actas = FormularioActa.objects.filter(
        tipo_acta_id_tipo_acta=estado).order_by('id')
    context = {'actas': actas}
    return render(request, 'taller/acta_retiro/acta_rechazo.html', context)


@login_required(login_url='login')
def CreateActaRechazo(request, id):
    data = dict()
    with connection.cursor() as cursor:
        cursor.execute("SELECT S.TALLER_ID_TALLER, S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) WHERE(S.TALLER_ID_TALLER = T.ID AND S.ID=" + id + ")")
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
        cursor.execute("SELECT S.DESCRIPCION,S.GRUA_PATENTE_GRUA,S.POLIZA_ID_POLIZA,S.ASEGURADO_RUT_ASEGURADO,F.ID,F.FECHA_HORA,F.OBSERVACIONES,V.PATENTE_VEHICULO,V.MODELO,V.ANIO,V.NRO_MOTOR,A.PRIMER_NOMBRE,A.PRIMER_APELLIDO,A.CORREO,A.TELEFONO,T.NOMBRE,T.RAZON_SOCIAL,T.TELEFONO,T.CORREO,M.NOMBRE,S.ID FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_FORMULARIOACTA F ON (S.ID=F.SINIESTRO_ID) JOIN DASHBOARD_VEHICULO V ON (S.ASEGURADO_RUT_ASEGURADO=V.ASEGURADO_RUT_ASEGURADO) JOIN DASHBOARD_ASEGURADO A ON (S.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO) JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_MARCA M ON (V.MARCA_ID_MARCA=M.ID) WHERE(f.tipo_acta_id_tipo_acta=1 AND S.ID="+pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'taller/acta_retiro/pdf/acta_pdf_rechazo.html', {'dato': dato})

def actaRechazoPdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '1in',
        'margin-bottom': '0.5in',
        'margin-left': '1in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/actaRechazoViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ActaRechazo.pdf" '
    return response

# INFORME DE DAÑOS
@login_required(login_url='login')
def InformeDañosView(request):
    estado = get_object_or_404(EstadoSiniestro, id=2)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/informe_daños.html', context)


@login_required(login_url='login')
def PresupuestoView(request):
    estado = get_object_or_404(EstadoSiniestro, id=3)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/presupuesto.html', context)


# @login_required(login_url='login')
# def VerActaRecepcion(request):
#     datosSiniestros = Siniestro.objects.raw('SELECT * FROM Platform')
#     datosSiniestros = Siniestro.objects.get(id=id)
#     actaRecepcion = FormularioActa.objects.filter(id=datosSiniestros).order_by('id')
#
#
#     context = {'actaRecepcion': actaRecepcion, 'datosSiniestros':datosSiniestros }
#     print(actaRecepcion)
#     return render(request, 'taller/acta_recepcion/acta_pdf.html', context)
#
#
