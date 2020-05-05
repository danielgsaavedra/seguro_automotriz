from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from dashboard.models import Usuario
from .forms import UsuarioRegisterForm

#CRUD USUARIOS
def SaveAllUsuario(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            usuarios = Usuario.objects.filter(
                is_active=True).order_by('rol')
            context = {'usuarios': usuarios,'form':form}
            data['usuarios'] = render_to_string(
                'registration/usuarios/usuarios_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)

#READ
def UsuariosView(request):
    usuarios = Usuario.objects.all().order_by('rol')
    context = {'usuarios': usuarios}
    return render(request, 'registration/usuarios/usuarios.html', context)

#CREATE
def UsuarioCreate(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
    else:
        form = UsuarioRegisterForm()
    return SaveAllUsuario(request, form, 'registration/usuarios/usuario_create.html')

class LoginPageView(TemplateView):
    template_name = "registration/login.html"


class RegisterPageView(TemplateView):
    template_name = "registration/registro.html"

