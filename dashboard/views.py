from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from .models import Usuario, Taller, Asegurado, Vehiculo, Poliza, Siniestro
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import PolizaForm, AseguradoForm, DeshabilitarAseguradoForm, VehiculoForm, SiniestroForm

# Create your views here.


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'


def TallerView(request):
    taller = Taller.objects.all().order_by('id_taller')
    context = {'taller': taller}
    return render(request, 'dashboard/taller.html', context)


def UsuariosView(request):
    usuarios = Usuario.objects.all().order_by('rol_id_rol')
    context = {'usuarios': usuarios}
    return render(request, 'dashboard/usuarios.html', context)


# Crud Asegurados
def SaveAllAsegurado(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            asegurados = Asegurado.objects.all().order_by('fecha_nacimiento')
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


def AseguradosView(request):
    asegurados = Asegurado.objects.all().order_by('fecha_nacimiento')
    context = {'asegurados': asegurados}
    return render(request, 'dashboard/asegurados/asegurado.html', context)

# Create


def AseguradoCreate(request):
    if request.method == 'POST':
        form = AseguradoForm(request.POST)
    else:
        form = AseguradoForm()
    return SaveAllAsegurado(request, form, 'dashboard/asegurados/asegurado_create.html')

# Update


def AseguradoUpdate(request, id):
    asegurado = get_object_or_404(Asegurado, rut_asegurado=id)
    if request.method == 'POST':
        form = AseguradoForm(request.POST, instance=asegurado)
    else:
        form = AseguradoForm(instance=asegurado)
    return SaveAllAsegurado(request, form, 'dashboard/asegurados/asegurado_update.html')

# Delete


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
            asegurados = Asegurado.objects.all().order_by('fecha_nacimiento')
            context = {'asegurados': asegurados}
            data['asegurados'] = render_to_string(
                'dashboard/asegurados/asegurado_2.html', context)
    else:
        form = DeshabilitarAseguradoForm(instance=asegurado)
        data['form_is_valid'] = False
        context = {'asegurado': asegurado,'form':form}
        data['html_form'] = render_to_string(
            'dashboard/asegurados/asegurado_delete.html', context, request=request)
    return JsonResponse(data)

# Crud Vehículos


def SaveAllVehiculo(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            vehiculos = Vehiculo.objects.all().order_by('anio')
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


def VehiculosView(request):
    vehiculos = Vehiculo.objects.all().order_by('anio')
    context = {'vehiculos': vehiculos}
    return render(request, 'dashboard/vehiculos/vehiculo.html', context)

# Create


def VehiculoCreate(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
    else:
        form = VehiculoForm()
    return SaveAllVehiculo(request, form, 'dashboard/vehiculos/vehiculo_create.html')


# Update


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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            polizas = Poliza.objects.all().order_by('-id_poliza')
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


def PolizasView(request):
    polizas = Poliza.objects.all().order_by('-id_poliza')
    context = {'polizas': polizas}
    return render(request, 'dashboard/polizas/poliza.html', context)

# Create


def CreatePoliza(request):
    if request.method == 'POST':
        form = PolizaForm(request.POST)
    else:
        form = PolizaForm()
    return SaveAllPoliza(request, form, 'dashboard/polizas/poliza_create.html')

# Update


def UpdatePoliza(request, id):
    poliza = get_object_or_404(Poliza, id_poliza=id)
    if request.method == 'POST':
        form = PolizaForm(request.POST, instance=poliza)
    else:
        form = PolizaForm(instance=poliza)
    return SaveAllPoliza(request, form, 'dashboard/polizas/poliza_update.html')

# Delete


def DeletePoliza(request, id):
    data = dict()
    poliza = get_object_or_404(Poliza, id_poliza=id)
    if request.method == 'POST':
        poliza.delete()
        data['form_is_valid'] = True
        polizas = Poliza.objects.all()
        context = {'polizas': polizas}
        data['polizas'] = render_to_string(
            'dashboard/polizas/poliza_2.html', context)
    else:
        context = {'poliza': poliza}
        data['html_form'] = render_to_string(
            'dashboard/polizas/poliza_delete.html', context, request=request)
    return JsonResponse(data)


# Crud Siniestro
def SaveAllSiniestro(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            siniestros = Siniestro.objects.all().order_by('-nro_siniestro')
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
def SiniestroView(request):
    siniestros = Siniestro.objects.all().order_by('-nro_siniestro')
    context = {'siniestros': siniestros}
    return render(request, 'dashboard/siniestros/siniestro.html', context)

# # Create


def CreateSiniestro(request):
    if request.method == 'POST':
        form = SiniestroForm(request.POST)
    else:
        form = SiniestroForm()
    return SaveAllSiniestro(request, form, 'dashboard/siniestros/siniestro_create.html')

# # Update


def UpdateSiniestro(request, id):
    siniestro = get_object_or_404(Siniestro, nro_siniestro=id)
    if request.method == 'POST':
        form = SiniestroForm(request.POST, instance=siniestro)
    else:
        form = SiniestroForm(instance=siniestro)
    return SaveAllSiniestro(request, form, 'dashboard/siniestros/siniestro_update.html')

# # Delete


def DeleteSiniestro(request, id):
    data = dict()
    siniestro = get_object_or_404(Siniestro, nro_siniestro=id)
    if request.method == 'POST':
        siniestro.delete()
        data['form_is_valid'] = True
        siniestro = Siniestro.objects.all()
        context = {'siniestros': siniestros}
        data['siniestros'] = render_to_string(
            'dashboard/siniestros/siniestro_2.html', context)
    else:
        context = {'siniestro': siniestro}
        data['html_form'] = render_to_string(
            'dashboard/siniestros/siniestro_delete.html', context, request=request)
    return JsonResponse(data)
