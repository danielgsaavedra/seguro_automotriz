from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import timezone
from django.http import JsonResponse
from .forms import ActasForm
from dashboard.models import Siniestro, EstadoSiniestro, FormularioActa, TipoActa


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
def SiniestrosRecepcionView(request):
    estado = get_object_or_404(EstadoSiniestro, id=1)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/acta_recepcion/siniestro_recepcion.html', context)


@login_required(login_url='login')
def CreateActaRecepcion(request):
    if request.method == 'POST':
        form = ActasForm(request.POST)
    else:
        form = ActasForm()
    return SaveAllActaRecepcion(request, form, 'taller/acta_recepcion/acta_recepcion_create.html')

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
def SiniestrosRetiroView(request):
    estado = get_object_or_404(EstadoSiniestro, id=6)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/acta_retiro/siniestro_retiro.html', context)


@login_required(login_url='login')
def CreateActaRetiro(request):
    if request.method == 'POST':
        form = ActasForm(request.POST)
    else:
        form = ActasForm()
    return SaveAllActaRecepcion(request, form, 'taller/acta_retiro/acta_retiro_create.html')

# ACTA RECHAZO


@login_required(login_url='login')
def ActaRechazoView(request):
    estado = get_object_or_404(TipoActa, id=2)
    actas = FormularioActa.objects.filter(
        tipo_acta_id_tipo_acta=estado).order_by('id')
    context = {'actas': actas}
    return render(request, 'taller/acta_retiro/acta_rechazo.html', context)


@login_required(login_url='login')
def CreateActaRechazo(request):
    if request.method == 'POST':
        form = ActasForm(request.POST)
    else:
        form = ActasForm()
    return SaveAllActaRetiro(request, form, 'taller/acta_retiro/acta_rechazo_create.html')


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
