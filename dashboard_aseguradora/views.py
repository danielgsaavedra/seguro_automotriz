from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class ListarSiniestrosView(TemplateView):
    template_name = 'dashboard_aseguradora/listar-siniestros.html'

class DashboardView(TemplateView):
    template_name = 'dashboard_aseguradora/dashboard.html'