from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Usuario
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class SiniestrosView(TemplateView):
    template_name = 'dashboard/siniestros.html'
    
def UsuariosView(request):
    usuarios = Usuario.objects.all().order_by('rol_id_rol')
    context = {'usuarios': usuarios}
    return render(request, 'dashboard/usuarios.html', context)