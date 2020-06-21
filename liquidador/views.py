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
from dashboard.models import Taller, Asegurado, Vehiculo, Poliza, Siniestro, EstadoSiniestro, Usuario , EstadoPresupuesto,Presupuesto
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