from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Usuario, Taller

# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class SiniestrosView(TemplateView):
    template_name = 'dashboard/siniestros.html'

def TallerView(request):
    taller = Taller.objects.all().order_by('id_taller')
    context = {'taller': taller}
    return render(request, 'dashboard/taller.html', context)
    
def UsuariosView(request):
    usuarios = Usuario.objects.all().order_by('rol_id_rol')
    context = {'usuarios': usuarios}
    return render(request, 'dashboard/usuarios.html', context)
