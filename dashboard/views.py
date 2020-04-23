from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class SiniestrosView(TemplateView):
    template_name = 'dashboard/siniestros.html'