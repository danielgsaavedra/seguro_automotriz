from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import timezone

from dashboard.models import Siniestro, EstadoSiniestro


@login_required(login_url='login')
def ActaRecepcionView(request):
    estado = get_object_or_404(EstadoSiniestro, id=1)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/acta_recepcion.html', context)

@login_required(login_url='login')
def ActaRetiroView(request):
    estado = get_object_or_404(EstadoSiniestro, id=6)
    siniestros = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=estado).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'taller/acta_retiro.html', context)

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