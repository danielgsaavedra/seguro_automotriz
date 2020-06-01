from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Taller, Asegurado, Vehiculo, Poliza, Siniestro, EstadoSiniestro, Usuario
from .forms import PolizaForm,PolizaFormUpdate, AseguradoForm, DeshabilitarAseguradoForm, VehiculoForm, SiniestroForm,SiniestroFormUpdate,DeshabilitarPolizaForm, DeshabilitarSiniestroForm, TallerForm, DeshabilitarTallerForm
from django.db.models import Q
from django.db.models import Count
from django.db import connection
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@method_decorator(login_required(login_url='login'), name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs1"] = Siniestro.objects.values('tipo_accidente_id_tipo_acc').annotate(
            dcount=Count('tipo_accidente_id_tipo_acc'))
        context["qs2"] = Siniestro.objects.values('est_siniestro_id_est_siniestro').annotate(
            dcount=Count('est_siniestro_id_est_siniestro'))
        return context


# Crud Asegurados


def SaveAllAsegurado(request, form, template_name):
    data = dict()
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            asegurados = Asegurado.objects.all().exclude(estado=0).filter(
                usuario_rut_usuario=user).order_by('rut_asegurado')
            context = {'asegurados': asegurados}
            data['asegurados'] = render_to_string(
                'dashboard/asegurados/asegurado_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Read

@login_required(login_url='login')
def AseguradosView(request):
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    asegurados = Asegurado.objects.all().exclude(estado=0).filter(
        usuario_rut_usuario=user).order_by('rut_asegurado')
    context = {'asegurados': asegurados}
    return render(request, 'dashboard/asegurados/asegurado.html', context)


# Listar usuarios Deshabilitados


def AseguradosDisableView(request):
    aseguradosDisable = Asegurado.objects.filter(
        estado=0).order_by('rut_asegurado')
    context = {'aseguradosDisable': aseguradosDisable}
    return render(request, 'dashboard/asegurados/asegurado_disabled.html', context)


# Create
@login_required(login_url='login')
def AseguradoCreate(request):
    if request.method == 'POST':
        form = AseguradoForm(request.POST)
        asegurado = form.save(commit=False)
        asegurado.usuario_rut_usuario = request.user
    else:
        form = AseguradoForm()
    return SaveAllAsegurado(request, form, 'dashboard/asegurados/asegurado_create.html')


# Update

@staff_member_required(login_url='login')
def AseguradoUpdate(request, id):
    asegurado = get_object_or_404(Asegurado, rut_asegurado=id)
    if request.method == 'POST':
        form = AseguradoForm(request.POST, instance=asegurado)
    else:
        form = AseguradoForm(instance=asegurado)
    return SaveAllAsegurado(request, form, 'dashboard/asegurados/asegurado_update.html')


# Delete

@staff_member_required(login_url='login')
def AseguradoDelete(request, id):
    data = dict()
    asegurado = get_object_or_404(Asegurado, rut_asegurado=id)
    if request.method == 'POST':
        form = DeshabilitarAseguradoForm(request.POST, instance=asegurado)
        if form.is_valid():
            asegurado = form.save(commit=False)
            asegurado.estado = "0"
            asegurado.save()
            data['form_is_valid'] = True
            asegurados = Asegurado.objects.filter(
                estado=1).order_by('fecha_nacimiento')
            context = {'asegurados': asegurados}
            data['asegurados'] = render_to_string(
                'dashboard/asegurados/asegurado_2.html', context)
    else:
        form = DeshabilitarAseguradoForm(instance=asegurado)
        data['form_is_valid'] = False
        context = {'asegurado': asegurado, 'form': form}
        data['html_form'] = render_to_string(
            'dashboard/asegurados/asegurado_delete.html', context, request=request)
    return JsonResponse(data)


# Reactivar asegurado


def ReactivateAsegurado(request, id):
    data = dict()
    aseguradoActivate = get_object_or_404(Asegurado, rut_asegurado=id)
    if request.method == 'POST':
        form = DeshabilitarAseguradoForm(
            request.POST, instance=aseguradoActivate)
        if form.is_valid():
            aseguradoActivate = form.save(commit=False)
            aseguradoActivate.estado = "1"
            aseguradoActivate.save()
            data['form_is_valid'] = True
            aseguradosDisable = Asegurado.objects.filter(
                estado=0).order_by('fecha_nacimiento')
            context = {'aseguradosDisable': aseguradosDisable}
            data['aseguradosDisable'] = render_to_string(
                'dashboard/asegurados/asegurado_disabled_2.html', context)
    else:
        form = DeshabilitarAseguradoForm(instance=aseguradoActivate)
        data['form_is_valid'] = False
        context = {'aseguradoActivate': aseguradoActivate, 'form': form}
        data['html_form'] = render_to_string(
            'dashboard/asegurados/asegurado_reactivate.html', context, request=request)
    return JsonResponse(data)


# Crud Vehículos


def SaveAllVehiculo(request, form, template_name):
    data = dict()
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            vehiculos = Vehiculo.objects.all().filter(
                usuario_rut_usuario=user).order_by('anio')
            context = {'vehiculos': vehiculos}
            data['vehiculos'] = render_to_string(
                'dashboard/vehiculos/vehiculo_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Read

@login_required(login_url='login')
def VehiculosView(request):
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    vehiculos = Vehiculo.objects.all().filter(
        usuario_rut_usuario=user).order_by('anio')
    context = {'vehiculos': vehiculos}
    return render(request, 'dashboard/vehiculos/vehiculo.html', context)


# Create

@login_required(login_url='login')
def VehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        vehiculo = form.save(commit=False)
        vehiculo.usuario_rut_usuario = request.user
    else:
        form = VehiculoForm()
    return SaveAllVehiculo(request, form, 'dashboard/vehiculos/vehiculo_create.html')


# Update

@staff_member_required(login_url='login')
def VehiculoUpdate(request, id):
    vehiculo = get_object_or_404(Vehiculo, patente_vehiculo=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
    else:
        form = VehiculoForm(instance=vehiculo)
    return SaveAllVehiculo(request, form, 'dashboard/vehiculos/vehiculo_update.html')


# Crud Pólizas


def SaveAllPoliza(request, form, template_name):
    data = dict()
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            with connection.cursor() as cursor:
                cursor.callproc('SP_VALIDAR_POLIZA')
            polizas = Poliza.objects.all().exclude(
                estado=0).filter(usuario_rut_usuario=user).order_by('id')
            context = {'polizas': polizas}
            data['polizas'] = render_to_string(
                'dashboard/polizas/poliza_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Read

@login_required(login_url='login')
def PolizasView(request):
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    with connection.cursor() as cursor:
        cursor.callproc('SP_VALIDAR_POLIZA')
    polizas = Poliza.objects.all().exclude(
        estado=0).filter(usuario_rut_usuario=user).order_by('id')
    context = {'polizas': polizas}
    return render(request, 'dashboard/polizas/poliza.html', context)


# Listar polizas disabled
def PolizasDisableView(request):
    polizasDisable = Poliza.objects.filter(estado=0).order_by('id')
    context = {'polizasDisable': polizasDisable}
    return render(request, 'dashboard/polizas/poliza_disabled.html', context)


# Create


@login_required(login_url='login')
def CreatePoliza(request):
    if request.method == 'POST':
        form = PolizaForm(request.POST)
        poliza = form.save(commit=False)
        poliza.usuario_rut_usuario = request.user
    else:
        form = PolizaForm()
    return SaveAllPoliza(request, form, 'dashboard/polizas/poliza_create.html')


def load_patentes(request):
    rut_asegurado = request.GET.get('rut')
    patentes = Vehiculo.objects.filter(asegurado_rut_asegurado=rut_asegurado)
    options = '<option value=""  selected="selected">---------</option>'

    for patente in patentes:
        options += '<option value="%s">%s</option>' % (
            patente,
            patente
        )

    response = {}
    response['patentes'] = options
    return JsonResponse(response)


# Update

@staff_member_required(login_url='login')
def UpdatePoliza(request, id):
    poliza = get_object_or_404(Poliza, id=id)
    if request.method == 'POST':
        form = PolizaFormUpdate(request.POST, instance=poliza)
    else:
        form = PolizaFormUpdate(instance=poliza)
    return SaveAllPoliza(request, form, 'dashboard/polizas/poliza_update.html')


# Delete

@staff_member_required(login_url='login')
def DeletePoliza(request, id):
    data = dict()
    poliza = get_object_or_404(Poliza, id=id)
    if request.method == 'POST':
        form = DeshabilitarPolizaForm(request.POST, instance=poliza)
        if form.is_valid():
            poliza = form.save(commit=False)
            poliza.estado = "0"
            poliza.save()
            data['form_is_valid'] = True
            polizas = Poliza.objects.filter(estado=1).order_by('id')
            context = {'polizas': polizas}
            data['polizas'] = render_to_string(
                'dashboard/polizas/poliza_2.html', context)
    else:
        form = DeshabilitarPolizaForm(instance=poliza)
        data['form_is_valid'] = False
        context = {'poliza': poliza, 'form': form}
        data['html_form'] = render_to_string(
            'dashboard/polizas/poliza_delete.html', context, request=request)
    return JsonResponse(data)


def ReactivatePoliza(request, id):
    data = dict()
    polizaActivate = get_object_or_404(Poliza, id=id)
    if request.method == 'POST':
        form = DeshabilitarPolizaForm(request.POST, instance=polizaActivate)
        if form.is_valid():
            polizaActivate = form.save(commit=False)
            polizaActivate.estado = "1"
            polizaActivate.save()
            data['form_is_valid'] = True
            polizasDisable = Poliza.objects.filter(estado=0).order_by('id')
            context = {'polizasDisable': polizasDisable}
            data['polizasDisable'] = render_to_string(
                'dashboard/polizas/poliza_disabled_2.html', context)
    else:
        form = DeshabilitarPolizaForm(instance=polizaActivate)
        data['form_is_valid'] = False
        context = {'polizaActivate': polizaActivate, 'form': form}
        data['html_form'] = render_to_string(
            'dashboard/polizas/poliza_reactivate.html', context, request=request)
    return JsonResponse(data)


# Crud Siniestro
def SaveAllSiniestro(request, form, template_name):
    data = dict()
    estado = get_object_or_404(EstadoSiniestro, id=7)
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            siniestros = Siniestro.objects.all().exclude(
                est_siniestro_id_est_siniestro=estado).filter(usuario_rut_usuario=user).order_by('id')
            context = {'siniestros': siniestros}
            data['siniestros'] = render_to_string(
                'dashboard/siniestros/siniestro_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Read
@login_required(login_url='login')
def SiniestroView(request):
    estado = get_object_or_404(EstadoSiniestro, id=7)
    with connection.cursor() as cursor:
        cursor.callproc('SP_VALIDAR_POLIZA')
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    siniestros = Siniestro.objects.all().exclude(
        est_siniestro_id_est_siniestro=estado).filter(usuario_rut_usuario=user).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'dashboard/siniestros/siniestro.html', context)


# Listar siniestros finalizandos
def SiniestroDisabledView(request):
    siniestrosDisable = Siniestro.objects.filter(
        est_siniestro_id_est_siniestro=7).order_by('id')
    context = {'siniestrosDisable': siniestrosDisable}
    return render(request, 'dashboard/siniestros/siniestro_disabled.html', context)


# # Create


@login_required(login_url='login')
def CreateSiniestro(request):
    estado = get_object_or_404(EstadoSiniestro, id=1)
    if request.method == 'POST':
        form = SiniestroForm(request.POST)
        siniestro = form.save(commit=False)
        siniestro.usuario_rut_usuario = request.user
        siniestro.est_siniestro_id_est_siniestro = estado
    else:
        form = SiniestroForm()
    return SaveAllSiniestro(request, form, 'dashboard/siniestros/siniestro_create.html')


def load_poliza(request):
    rut_asegurado = request.GET.get('rut_ase')
    polizas = Poliza.objects.filter(
        Q(asegurado_rut_asegurado=rut_asegurado) & Q(vigente=1))
    options = '<option value=""  selected="selected">---------</option>'
    for poliza in polizas:
        options += '<option value="%s">%s</option>' % (
            poliza,
            poliza
        )

    response = {}
    response['polizas'] = options
    return JsonResponse(response)


# # Update

@staff_member_required(login_url='login')
def UpdateSiniestro(request, id):
    siniestro = get_object_or_404(Siniestro, id=id)
    if request.method == 'POST':
        form = SiniestroFormUpdate(request.POST, instance=siniestro)
    else:
        form = SiniestroFormUpdate(instance=siniestro)
    return SaveAllSiniestro(request, form, 'dashboard/siniestros/siniestro_update.html')


# # Delete

@staff_member_required(login_url='login')
def DeleteSiniestro(request, id):
    data = dict()
    siniestro = get_object_or_404(Siniestro, id=id)
    estado = get_object_or_404(EstadoSiniestro, id=7)
    if request.method == 'POST':
        form = DeshabilitarSiniestroForm(request.POST, instance=siniestro)
        if form.is_valid():
            siniestro = form.save(commit=False)
            siniestro.est_siniestro_id_est_siniestro = estado
            siniestro.save()
            data['form_is_valid'] = True
            siniestros = Siniestro.objects.all().exclude(
                est_siniestro_id_est_siniestro=estado).order_by('id')
            context = {'siniestros': siniestros}
            data['siniestros'] = render_to_string(
                'dashboard/siniestros/siniestro_2.html', context)
    else:
        form = DeshabilitarSiniestroForm(instance=siniestro)
        data['form_is_valid'] = False
        context = {'siniestro': siniestro, 'form': form}
        data['html_form'] = render_to_string(
            'dashboard/siniestros/siniestro_delete.html', context, request=request)
    return JsonResponse(data)


# Crud Taller


def SaveAllTaller(request, form, template_name):
    data = dict()
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            talleres = Taller.objects.all().exclude(estado_delete=0).filter(
                usuario_rut_usuario=user).order_by('id')
            context = {'talleres': talleres}
            data['talleres'] = render_to_string(
                'dashboard/talleres/taller_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Listar

@login_required(login_url='login')
def TallerView(request):
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    with connection.cursor() as cursor:
        cursor.callproc('SP_ESTADO_TALLER')
    talleres = Taller.objects.all().exclude(estado_delete=0).filter(
        usuario_rut_usuario=user).order_by('id')
    context = {'talleres': talleres}
    return render(request, 'dashboard/talleres/taller.html', context)


# Listar talleres disabled
def TallerDisabledView(request):
    talleresDisable = Taller.objects.filter(estado_delete=0).order_by('id')
    context = {'talleresDisable': talleresDisable}
    return render(request, 'dashboard/talleres/taller_disabled.html', context)


# Crear

@login_required(login_url='login')
def CreateTaller(request):
    if request.method == 'POST':
        form = TallerForm(request.POST)
        taller = form.save(commit=False)
        taller.usuario_rut_usuario = request.user
        taller.estado = 1
    else:
        form = TallerForm()
    return SaveAllTaller(request, form, 'dashboard/talleres/taller_create.html')


# Actualizar

@staff_member_required(login_url='login')
def UpdateTaller(request, id):
    taller = get_object_or_404(Taller, id=id)
    if request.method == 'POST':
        form = TallerForm(request.POST, instance=taller)
    else:
        form = TallerForm(instance=taller)
    return SaveAllTaller(request, form, 'dashboard/talleres/taller_update.html')


# Borrar

@staff_member_required(login_url='login')
def DeleteTaller(request, id):
    data = dict()
    taller = get_object_or_404(Taller, id=id)
    if request.method == 'POST':
        form = DeshabilitarTallerForm(request.POST, instance=taller)
        if form.is_valid():
            taller = form.save(commit=False)
            taller.estado_delete = "0"
            taller.save()
            data['form_is_valid'] = True
            talleres = Taller.objects.filter(
                estado_delete=1).order_by('id')
            context = {'talleres': talleres}
            data['talleres'] = render_to_string(
                'dashboard/talleres/taller_2.html', context)
    else:
        form = DeshabilitarTallerForm(instance=taller)
        data['form_is_valid'] = False
        context = {'taller': taller, 'form': form}
        data['html_form'] = render_to_string(
            'dashboard/talleres/taller_delete.html', context, request=request)
    return JsonResponse(data)


def ReactivateTaller(request, id):
    data = dict()
    tallerActivate = get_object_or_404(Taller, id=id)
    if request.method == 'POST':
        form = DeshabilitarTallerForm(request.POST, instance=tallerActivate)
        if form.is_valid():
            tallerActivate = form.save(commit=False)
            tallerActivate.estado_delete = "1"
            tallerActivate.save()
            data['form_is_valid'] = True
            talleresDisable = Taller.objects.filter(
                estado_delete=0).order_by('id')
            context = {'talleresDisable': talleresDisable}
            data['talleresDisable'] = render_to_string(
                'dashboard/talleres/taller_disabled_2.html', context)
    else:
        form = DeshabilitarTallerForm(instance=tallerActivate)
        data['form_is_valid'] = False
        context = {'tallerActivate': tallerActivate, 'form': form}
        data['html_form'] = render_to_string(
            'dashboard/talleres/taller_reactivate.html', context, request=request)
    return JsonResponse(data)


def AseguradoConsultaView(request):
    queryset1 = request.GET.get("rut_asegurado")
    queryset2 = request.GET.get("n_poliza")

    if queryset1:
        siniestros = Siniestro.objects.filter(
            Q(asegurado_rut_asegurado=queryset1) &
            Q(poliza_id_poliza=queryset2)
        )
    else:
        siniestros = Siniestro.objects.none()

    return render(request, 'dashboard/asegurados/asegurado_consulta.html', {'siniestros': siniestros})


class HomeView(TemplateView):
    template_name = 'dashboard/home.html'
