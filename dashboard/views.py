from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class ListarSiniestrosView(TemplateView):
    template_name = 'dashboard/listar_siniestro.html'