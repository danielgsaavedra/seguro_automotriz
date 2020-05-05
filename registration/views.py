from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from dashboard.models import Usuario
from .forms import UsuarioRegisterForm,UsuarioFormUpdate,DeshabilitarUsuarioForm

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
@staff_member_required(login_url='login')
def UsuariosView(request):
    usuarios = Usuario.objects.filter(is_active=True).order_by('rol')
    context = {'usuarios': usuarios}
    return render(request, 'registration/usuarios/usuarios.html', context)

#Listar usuarios Inactivos
@staff_member_required(login_url='login')
def UsuariosDisableView(request):
    usuariosDisable = Usuario.objects.filter(is_active=False).order_by('rol')
    context = {'usuariosDisable': usuariosDisable}
    return render(request, 'registration/usuarios/usuario_disabled.html', context)

#Reactivar Usuario
@staff_member_required(login_url='login')
def ReactivateUsuario(request, id):
    data = dict()
    usuarioActivate = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = DeshabilitarUsuarioForm(request.POST, instance=usuarioActivate)
        if form.is_valid():
            usuarioActivate = form.save(commit=False)
            usuarioActivate.is_active = "1"
            usuarioActivate.save()
            data['form_is_valid'] = True
            usuariosDisable = Usuario.objects.filter(is_active=0).order_by('rol')
            context = {'usuariosDisable': usuariosDisable}
            data['usuariosDisable'] = render_to_string(
                'registration/usuarios/usuario_disabled_2.html.html', context)
    else:
        form = DeshabilitarUsuarioForm(instance=usuarioActivate)
        data['form_is_valid'] = False
        context = {'usuarioActivate': usuarioActivate, 'form': form}
        data['html_form'] = render_to_string(
            'registration/usuarios/usuario_reactivate.html', context, request=request)
    return JsonResponse(data)


#CREATE
@staff_member_required(login_url='login')
def UsuarioCreate(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
    else:
        form = UsuarioRegisterForm()
    return SaveAllUsuario(request, form, 'registration/usuarios/usuario_create.html')

#UPDATE
@staff_member_required(login_url='login')
def UsuarioUpdate(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioFormUpdate(request.POST, instance=usuario)
    else:
        form = UsuarioFormUpdate(instance=usuario)
    return SaveAllUsuario(request, form, 'registration/usuarios/usuario_update.html')


@staff_member_required(login_url='login')
def UsuarioDelete(request, id):
    data = dict()
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = DeshabilitarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_active = False
            usuario.save()
            data['form_is_valid'] = True
            usuarios = Usuario.objects.filter(is_active=True).order_by('rol')
            context = {'usuarios': usuarios}
            data['usuarios'] = render_to_string(
                'registration/usuarios/usuarios_2.html', context)
    else:
        form = DeshabilitarUsuarioForm(instance=usuario)
        data['form_is_valid'] = False
        context = {'usuario': usuario, 'form': form}
        data['html_form'] = render_to_string(
            'registration/usuarios/usuario_delete.html', context, request=request)
    return JsonResponse(data)



class LoginPageView(TemplateView):
    template_name = "registration/login.html"


class RegisterPageView(TemplateView):
    template_name = "registration/registro.html"

