from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import datetime
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from dashboard.models import Taller, Asegurado, Vehiculo, Poliza, Siniestro, EstadoSiniestro, Usuario, \
    EstadoPresupuesto, Presupuesto, TipoActa, FormularioActa, InformeDano, TipoPlan
from .forms import TipoPlanForm, DeshabilitarTipoPlanForm, AproRechPresupuestoForm
from django.db.models import Q
from django.db.models import Count
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import pdfkit
from django.http import HttpResponse


# Create your views here.

@login_required(login_url='login')
def SiniestroView(request):
    estado = get_object_or_404(EstadoSiniestro, id=7)
    estado1 = get_object_or_404(EstadoSiniestro, id=8)
    estado3 = get_object_or_404(EstadoSiniestro, id=5)

    siniestros = Siniestro.objects.all().exclude(
        Q(est_siniestro_id_est_siniestro=estado) |
        Q(est_siniestro_id_est_siniestro=estado1) |
        Q(est_siniestro_id_est_siniestro=estado3)
    ).order_by('id')
    siniestrosDisable = Siniestro.objects.aggregate(
        dcount=Count('id', filter=Q(est_siniestro_id_est_siniestro=7)))
    siniestrosPendientes = Siniestro.objects.aggregate(
        dcount=Count('id', filter=Q(est_siniestro_id_est_siniestro=8)))
    siniestrosRechazados = Siniestro.objects.aggregate(
        dcount=Count('id', filter=Q(est_siniestro_id_est_siniestro=5)))
    context = {'siniestros': siniestros,
               'siniestrosDisable': siniestrosDisable,
               'siniestrosPendientes': siniestrosPendientes,
               'siniestrosRechazados': siniestrosRechazados}
    return render(request, 'liquidador/siniestros/siniestro.html', context)


def SiniestroDisabledView(request):
    siniestrosDisable = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=7).order_by('id')
    context = {'siniestrosDisable': siniestrosDisable}
    return render(request, 'liquidador/siniestros/siniestro_disabled.html', context)


def SiniestroRechazadosView(request):
    siniestrosRechazo = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=5).order_by('id')
    context = {'siniestrosRechazo': siniestrosRechazo}
    return render(request, 'liquidador/siniestros/siniestro_rechazo.html', context)


def SiniestroPendientesView(request):
    siniestrosPendiente = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=8).order_by('id')
    context = {'siniestrosPendiente': siniestrosPendiente}
    return render(request, 'liquidador/siniestros/siniestro_pendiente.html', context)


@login_required(login_url='login')
def PresupuestoView(request):
    estado = get_object_or_404(EstadoPresupuesto, id=3)
    presupuestos = Presupuesto.objects.filter(
        estado_id_est_presupuesto=estado).order_by('id')
    presupuestosRechazados = Presupuesto.objects.aggregate(
        dcount=Count('id', filter=Q(estado_id_est_presupuesto=2)))
    presupuestosAprobados = Presupuesto.objects.aggregate(
        dcount=Count('id', filter=Q(estado_id_est_presupuesto=1)))
    context = {'presupuestos': presupuestos,
               'presupuestosRechazados': presupuestosRechazados,
               'presupuestosAprobados': presupuestosAprobados}
    return render(request, 'liquidador/presupuestos/presupuestos_view.html', context)


@login_required(login_url='login')
def PresupuestoAprobadoView(request):
    estado = get_object_or_404(EstadoPresupuesto, id=1)
    presupuestos = Presupuesto.objects.filter(
        estado_id_est_presupuesto=estado).order_by('id')
    context = {'presupuestos': presupuestos}
    return render(request, 'liquidador/presupuestos/presupuestos_aprobados.html', context)


@login_required(login_url='login')
def PresupuestoRechazadoView(request):
    estado = get_object_or_404(EstadoPresupuesto, id=2)
    presupuestos = Presupuesto.objects.filter(
        estado_id_est_presupuesto=estado).order_by('id')
    context = {'presupuestos': presupuestos}
    return render(request, 'liquidador/presupuestos/presupuestos_rechazados.html', context)


@login_required(login_url='login')
def PresupuestoAproRechView(request, id):
    presupuesto = get_object_or_404(Presupuesto, id=id)
    context = {'presupuesto': presupuesto}
    return render(request, 'liquidador/presupuestos/presupuestos_apro_recha_view.html', context)


@staff_member_required(login_url='login')
def AprobarPresupuesto(request, id):
    data = dict()
    presupuesto = get_object_or_404(Presupuesto, id=id)
    estado = get_object_or_404(EstadoPresupuesto, id=1)
    if request.method == 'POST':
        form = AproRechPresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            pre = form.save(commit=False)
            pre.estado_id_est_presupuesto = estado
            pre.usuario_rut_usuario = request.user
            pre.save()
            data['form_is_valid'] = True
            correo = EmailMessage(
                'SEGUROS VIRGOLINI: PRESUPUESTO APROBADO',
                'ESTIMADO/A {} {}.\n\nEL PRESUPUESTO N°{} ASOCIADO A SU SINIESTRO N°{} A SIDO APROBADO CON ÉXITO.\n\nSALUDOS CORDIALES.'.format(
                    presupuesto.siniestro_id.asegurado_rut_asegurado.primer_nombre,
                    presupuesto.siniestro_id.asegurado_rut_asegurado.primer_apellido,
                    presupuesto.id, presupuesto.siniestro_id.id),
                'no-contestar@hotmail.com',
                [presupuesto.siniestro_id.asegurado_rut_asegurado.correo],
                reply_to=['contacto.segurosvirgolini@gmail.com']
            )
            correo.send()

    else:
        form = AproRechPresupuestoForm(instance=presupuesto)
        data['form_is_valid'] = False
        context = {'presupuesto': presupuesto, 'form': form}
        data['html_form'] = render_to_string(
            'liquidador/presupuestos/aprobar_presupuesto.html', context, request=request)
    return JsonResponse(data)


@staff_member_required(login_url='login')
def RechazarPresupuesto(request, id):
    data = dict()
    presupuesto = get_object_or_404(Presupuesto, id=id)
    estado = get_object_or_404(EstadoPresupuesto, id=2)
    if request.method == 'POST':
        form = AproRechPresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            pre = form.save(commit=False)
            pre.estado_id_est_presupuesto = estado
            pre.usuario_rut_usuario = request.user
            pre.save()
            data['form_is_valid'] = True
            with connection.cursor() as cursor:
                cursor.callproc('SP_CAMBIAR_GARANTIA')
            correo = EmailMessage(
                'SEGUROS VIRGOLINI: PRESUPUESTO RECHAZADO',
                'ESTIMADO/A {} {}.\n\nEL PRESUPUESTO N°{} ASOCIADO A SU SINIESTRO N°{} A SIDO RECHAZADO.\n\nSALUDOS CORDIALES.'.format(
                    presupuesto.siniestro_id.asegurado_rut_asegurado.primer_nombre,
                    presupuesto.siniestro_id.asegurado_rut_asegurado.primer_apellido,
                    presupuesto.id, presupuesto.siniestro_id.id),
                'no-contestar@hotmail.com',
                [presupuesto.siniestro_id.asegurado_rut_asegurado.correo],
                reply_to=['contacto.segurosvirgolini@gmail.com']
            )
            correo.send()

    else:
        form = AproRechPresupuestoForm(instance=presupuesto)
        data['form_is_valid'] = False
        context = {'presupuesto': presupuesto, 'form': form}
        data['html_form'] = render_to_string(
            'liquidador/presupuestos/rechazar_presupuesto.html', context, request=request)
    return JsonResponse(data)


@login_required(login_url='login')
def ReportesView(request):
    recepcion = get_object_or_404(TipoActa, id=1)
    retiro = get_object_or_404(TipoActa, id=3)
    rechazo = get_object_or_404(TipoActa, id=2)

    actas_recepcion = FormularioActa.objects.filter(
        tipo_acta_id_tipo_acta=recepcion)
    actas_retiro = FormularioActa.objects.filter(tipo_acta_id_tipo_acta=retiro)
    actas_rechazo = FormularioActa.objects.filter(
        tipo_acta_id_tipo_acta=rechazo)
    informes_dano = InformeDano.objects.all()
    presupuestos = Presupuesto.objects.all()
    polizas = Poliza.objects.all().exclude(estado=0).order_by('id')

    context = {'presupuestos': presupuestos, 'actas_recepcion': actas_recepcion, 'actas_retiro': actas_retiro,
               'actas_rechazo': actas_rechazo, 'informes_dano': informes_dano, 'polizas': polizas}
    return render(request, 'liquidador/reportes/reportes.html', context)


@login_required(login_url='login')
def TipoPlanView(request):
    tipos_plan = TipoPlan.objects.all().exclude(estado=False).order_by('id')
    tipoPlanDisable = TipoPlan.objects.aggregate(
        dcount=Count('id', filter=Q(estado=0)))
    context = {'tipos_plan': tipos_plan,
               'tipoPlanDisable': tipoPlanDisable}
    return render(request, 'liquidador/tipoPlan/tipos_plan.html', context)


@login_required(login_url='login')
def TipoPlanInactivos(request):
    tipos_plan_disabled = TipoPlan.objects.filter(estado=False)
    context = {'tipos_plan_disabled': tipos_plan_disabled}
    return render(request, 'liquidador/tipoPlan/tipos_plan_disabled.html', context)


def SaveAllTipoPlan(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tipos_plan = TipoPlan.objects.all().exclude(estado=False).order_by('id')
            context = {'tipos_plan': tipos_plan}
            data['tipos_plan'] = render_to_string(
                'liquidador/tipoPlan/tipos_plan_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Read
@login_required(login_url='login')
def TipoPlanCreate(request):
    if request.method == 'POST':
        form = TipoPlanForm(request.POST)
        tipo_plan = form.save(commit=False)
        tipo_plan.usuario_rut_usuario = request.user
    else:
        form = TipoPlanForm()
    return SaveAllTipoPlan(request, form, 'liquidador/tipoPlan/tipo_plan_create.html')


@staff_member_required(login_url='login')
def TipoPlanUpdate(request, id):
    tipo_plan = get_object_or_404(TipoPlan, id=id)
    if request.method == 'POST':
        form = TipoPlanForm(request.POST, instance=tipo_plan)
        tipo_plan = form.save(commit=False)
        tipo_plan.usuario_rut_usuario = request.user
    else:
        form = TipoPlanForm(instance=tipo_plan)
    return SaveAllTipoPlan(request, form, 'liquidador/tipoPlan/tipo_plan_update.html')


@staff_member_required(login_url='login')
def TipoPlanDelete(request, id):
    data = dict()
    tipo_plan = get_object_or_404(TipoPlan, id=id)
    if request.method == 'POST':
        form = DeshabilitarTipoPlanForm(request.POST, instance=tipo_plan)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.estado = False
            plan.usuario_rut_usuario = request.user
            plan.save()
            data['form_is_valid'] = True
            tipos_plan = TipoPlan.objects.all().exclude(estado=False).order_by('id')
            context = {'tipos_plan': tipos_plan}
            data['tipos_plan'] = render_to_string(
                'liquidador/tipoPlan/tipos_plan_2.html', context)
    else:
        form = DeshabilitarTipoPlanForm(instance=tipo_plan)
        data['form_is_valid'] = False
        context = {'tipo_plan': tipo_plan, 'form': form}
        data['html_form'] = render_to_string(
            'liquidador/tipoPlan/tipo_plan_delete.html', context, request=request)
    return JsonResponse(data)


@staff_member_required(login_url='login')
def TipoPlanReactive(request, id):
    data = dict()
    tipo_plan = get_object_or_404(TipoPlan, id=id)
    if request.method == 'POST':
        form = DeshabilitarTipoPlanForm(request.POST, instance=tipo_plan)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.estado = True
            plan.usuario_rut_usuario = request.user
            plan.save()
            data['form_is_valid'] = True
            tipos_plan_disabled = TipoPlan.objects.all().exclude(estado=True).order_by('id')
            context = {'tipos_plan_disabled': tipos_plan_disabled}
            data['tipos_plan'] = render_to_string(
                'liquidador/tipoPlan/tipos_plan_disabled_2.html', context)
    else:
        form = DeshabilitarTipoPlanForm(instance=tipo_plan)
        data['form_is_valid'] = False
        context = {'tipo_plan': tipo_plan, 'form': form}
        data['html_form'] = render_to_string(
            'liquidador/tipoPlan/tipo_plan_reactive.html', context, request=request)
    return JsonResponse(data)


# todo Falta desarrollar aprobar y rechazar presupuesto


def PolizaViewPdf(request, pk):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT P.ID,P.VIGENTE,P.FECHA_INICIO,P.FECHA_FIN,U.RUT_USUARIO,U.PRIMER_NOMBRE,U.SEGUNDO_NOMBRE,U.PRIMER_APELLIDO,U.SEGUNDO_APELLIDO,P.ASEGURADO_RUT_ASEGURADO,A.PRIMER_NOMBRE,A.SEGUNDO_NOMBRE,A.PRIMER_APELLIDO,A.SEGUNDO_APELIIDO,A.CORREO,A.TELEFONO,A.DIRECCION,C.NOMBRE,T.NOMBRE,T.DESCRIPCION,T.VALOR,T.DEDUCIBLE,T.COBERTURA_MAX,V.PATENTE_VEHICULO,X.TIPO,M.NOMBRE,V.MODELO,V.ANIO,V.NRO_MOTOR FROM DASHBOARD_POLIZA P JOIN DASHBOARD_USUARIO U ON U.ID=P.USUARIO_RUT_USUARIO JOIN DASHBOARD_ASEGURADO A ON  P.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO JOIN DASHBOARD_COMUNA C ON C.ID=A.COMUNA_ID_COMUNA JOIN DASHBOARD_TIPOPLAN T ON P.TIPO_PLAN_ID_TIP_PLAN=T.ID JOIN DASHBOARD_VEHICULO V ON V.PATENTE_VEHICULO=P.VEHICULO_PATENTE_VEHICULO JOIN DASHBOARD_TIPOVEHICULO X ON X.ID=V.TIPO_VEHICULO_ID_TIPO_AUTO JOIN DASHBOARD_MARCA M ON M.ID=V.MARCA_ID_MARCA WHERE (P.ID=" + pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'liquidador/reportes/pdf/poliza_pdf.html', {'dato': dato})


def PolizaPdf(request, pk):
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
    pdf = pdfkit.from_url('http://127.0.0.1:8000/liquidador/PolizaViewPdf/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Poliza.pdf" '
    return response
