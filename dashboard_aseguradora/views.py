from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class DashboardAsegView(TemplateView):
    template_name = 'dashboard_aseguradora/dashboard.html'