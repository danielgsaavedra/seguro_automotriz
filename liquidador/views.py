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
from .forms import TipoPlanForm, DeshabilitarTipoPlanForm
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
    siniestros = Siniestro.objects.all().exclude(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'liquidador/siniestros/siniestro.html', context)


def SiniestroDisabledView(request):
    siniestrosDisable = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=7).order_by('id')
    context = {'siniestrosDisable': siniestrosDisable}
    return render(request, 'liquidador/siniestros/siniestro_disabled.html', context)


@login_required(login_url='login')
def PresupuestoView(request):
    estado = get_object_or_404(EstadoPresupuesto, id=3)
    presupuestos = Presupuesto.objects.filter(estado_id_est_presupuesto=estado).order_by('id')
    context = {'presupuestos': presupuestos}
    return render(request, 'liquidador/presupuestos/presupuestos_view.html', context)


@login_required(login_url='login')
def PresupuestoAprobadoView(request):
    estado = get_object_or_404(EstadoPresupuesto, id=1)
    presupuestos = Presupuesto.objects.filter(estado_id_est_presupuesto=estado).order_by('id')
    context = {'presupuestos': presupuestos}
    return render(request, 'liquidador/presupuestos/presupuestos_aprobados.html', context)


@login_required(login_url='login')
def PresupuestoRechazadoView(request):
    estado = get_object_or_404(EstadoPresupuesto, id=2)
    presupuestos = Presupuesto.objects.filter(estado_id_est_presupuesto=estado).order_by('id')
    context = {'presupuestos': presupuestos}
    return render(request, 'liquidador/presupuestos/presupuestos_rechazados.html', context)


@login_required(login_url='login')
def ReportesView(request):
    recepcion = get_object_or_404(TipoActa, id=1)
    retiro = get_object_or_404(TipoActa, id=3)
    rechazo = get_object_or_404(TipoActa, id=2)

    actas_recepcion = FormularioActa.objects.filter(tipo_acta_id_tipo_acta=recepcion)
    actas_retiro = FormularioActa.objects.filter(tipo_acta_id_tipo_acta=retiro)
    actas_rechazo = FormularioActa.objects.filter(tipo_acta_id_tipo_acta=rechazo)
    informes_dano = InformeDano.objects.all()
    presupuestos = Presupuesto.objects.all()

    context = {'presupuestos': presupuestos, 'actas_recepcion': actas_recepcion, 'actas_retiro': actas_retiro,
               'actas_rechazo': actas_rechazo, 'informes_dano': informes_dano}
    return render(request, 'liquidador/reportes/reportes.html', context)


@login_required(login_url='login')
def TipoPlanView(request):
    tipos_plan = TipoPlan.objects.all().exclude(estado=False).order_by('id')
    context = {'tipos_plan': tipos_plan}
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

# todo Implementar reactivacion de tipos de plan
# todo Falta desarrollar aprobar y rechazar presupuesto
# todo Se debe crear consulta SQL para pdf polizas
