from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import datetime
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .models import Taller, Asegurado, Vehiculo, Poliza, Siniestro, EstadoSiniestro, Usuario, FormularioActa, \
    Presupuesto, TipoActa, RegActas, RegAsegurado, RegGrua, RegInformeDano, RegSiniestro, RegPoliza, RegPresupuesto, \
    RegTaller, RegTipoPlan, RegUsuario, RegVehiculo, RegServicioGrua, ServicioGrua
from .forms import PolizaForm, PolizaFormUpdate, AseguradoForm, DeshabilitarAseguradoForm, VehiculoForm, SiniestroForm, \
    SiniestroFormUpdate, DeshabilitarPolizaForm, DeshabilitarSiniestroForm, TallerForm, DeshabilitarTallerForm, \
    AseguradoFormUpdate, VehiculoFormUpdate, SiniestroFotosUpdate, ServicioGruaForm
from django.db.models import Q
from django.db.models import Count
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import pdfkit
from django.http import HttpResponse


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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            asegurados = Asegurado.objects.all().exclude(estado=0).order_by('rut_asegurado')
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
    asegurados = Asegurado.objects.all().exclude(estado=0).order_by('rut_asegurado')
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
        form = AseguradoFormUpdate(request.POST, instance=asegurado)
    else:
        form = AseguradoFormUpdate(instance=asegurado)
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
                estado=1).order_by('rut_asegurado')
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
    user = get_object_or_404(Usuario, rut_usuario=request.user.rut_usuario)
    if request.method == 'POST':
        form = DeshabilitarAseguradoForm(
            request.POST, instance=aseguradoActivate)
        if form.is_valid():
            aseguradoActivate = form.save(commit=False)
            aseguradoActivate.estado = "1"
            aseguradoActivate.save()
            data['form_is_valid'] = True
            aseguradosDisable = Asegurado.objects.filter(
                Q(usuario_rut_usuario=user) &
                Q(estado=0)
            ).order_by('fecha_nacimiento')
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

# Read

@login_required(login_url='login')
def VehiculosView(request, id):
    vehiculos = Vehiculo.objects.all().filter(
        asegurado_rut_asegurado=id)
    context = {'vehiculos': vehiculos}
    return render(request, 'dashboard/vehiculos/vehiculo.html', context)


# Create


@login_required(login_url='login')
def VehiculoCreate(request, id):
    data = dict()
    asegurado = get_object_or_404(Asegurado, rut_asegurado=id)
    print(asegurado.rut_asegurado)
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.usuario_rut_usuario = request.user
            vehiculo.asegurado_rut_asegurado = asegurado
            vehiculo.save()
            data['form_is_valid'] = True
            vehiculos = Vehiculo.objects.all()
            context = {'vehiculos': vehiculos}
            data['vehiculos'] = render_to_string(
                'dashboard/vehiculos/vehiculo_2.html', context)
        else:
            data['form_is_valid'] = False
    else:
        form = VehiculoForm()

    context = {'form': form, 'asegurado': asegurado}
    data['html_form'] = render_to_string(
        'dashboard/vehiculos/vehiculo_create.html', context, request=request)
    return JsonResponse(data)


# Update


@staff_member_required(login_url='login')
def VehiculoUpdate(request, id):
    data = dict()
    vehiculo = get_object_or_404(Vehiculo, patente_vehiculo=id)
    if request.method == 'POST':
        form = VehiculoFormUpdate(request.POST, instance=vehiculo)
        if form.is_valid():
            data['form_is_valid'] = True
            vehiculos = Vehiculo.objects.all().filter(
                asegurado_rut_asegurado=vehiculo.asegurado_rut_asegurado).order_by('anio')
            context = {'vehiculos': vehiculos}
            data['vehiculos'] = render_to_string(
                'dashboard/vehiculos/vehiculo_2.html', context)

        else:
            data['form_is_valid'] = False

    else:
        form = VehiculoFormUpdate(instance=vehiculo)

    context = {'form': form, 'vehiculo': vehiculo}
    data['html_form'] = render_to_string(
        'dashboard/vehiculos/vehiculo_update.html', context, request=request)
    return JsonResponse(data)


# Crud Pólizas


def SaveAllPoliza(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            with connection.cursor() as cursor:
                cursor.callproc('SP_VALIDAR_POLIZA')
            polizas = Poliza.objects.all().exclude(
                estado=0).order_by('id')
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
    with connection.cursor() as cursor:
        cursor.callproc('SP_VALIDAR_POLIZA')
    polizas = Poliza.objects.all().exclude(
        estado=0).order_by('id')
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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            siniestros = Siniestro.objects.all().exclude(
                est_siniestro_id_est_siniestro=estado).order_by('id')
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
    siniestros = Siniestro.objects.all().exclude(
        est_siniestro_id_est_siniestro=estado).order_by('id')
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
    x = datetime.datetime.now()
    rut = request.POST.get('asegurado_rut_asegurado', '')
    id_poliza = request.POST.get('poliza_id_poliza', '')
    id_taller = request.POST.get('taller_id_taller', '')
    estado = get_object_or_404(EstadoSiniestro, id=1)

    if request.method == 'POST':
        asegurado = get_object_or_404(Asegurado, rut_asegurado=rut)
        poliza = get_object_or_404(Poliza, id=id_poliza)
        taller = get_object_or_404(Taller, id=id_taller)
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
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            talleres = Taller.objects.all().exclude(estado_delete=0).order_by('id')
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
    with connection.cursor() as cursor:
        cursor.callproc('SP_ESTADO_TALLER')
    talleres = Taller.objects.all().exclude(estado_delete=0).order_by('id')
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
            talleres = Taller.objects.filter(estado_delete=1).order_by('id')
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


def HomeView(request):
    acta_recepcion = get_object_or_404(TipoActa, id=1)
    acta_retiro = get_object_or_404(TipoActa, id=3)
    acta_rechazo = get_object_or_404(TipoActa, id=2)
    reg_asegurados = RegAsegurado.objects.all()
    reg_vehiculos = RegVehiculo.objects.all()
    reg_polizas = RegPoliza.objects.all()
    reg_siniestros = RegSiniestro.objects.all()
    reg_talleres = RegTaller.objects.all()
    reg_usuarios = RegUsuario.objects.all()
    reg_actas_recepcion = RegActas.objects.filter(
        Q(tipo_acta_id_tipo_acta=acta_recepcion) &
        Q(taller_id_taller=request.user.taller_id_taller)
    )
    reg_actas_retiro = RegActas.objects.filter(
        Q(tipo_acta_id_tipo_acta=acta_retiro) &
        Q(taller_id_taller=request.user.taller_id_taller)
    )
    reg_actas_rechazo = RegActas.objects.filter(
        Q(tipo_acta_id_tipo_acta=acta_rechazo) &
        Q(taller_id_taller=request.user.taller_id_taller)
    )
    reg_informes = RegInformeDano.objects.filter(
        taller_id_taller=request.user.taller_id_taller)
    reg_presupuestos = RegPresupuesto.objects.filter(
        taller_id_taller=request.user.taller_id_taller)
    reg_siniestros_taller = RegSiniestro.objects.filter(
        taller_id_taller=request.user.taller_id_taller)
    reg_gruas = RegGrua.objects.all()
    reg_servicio_gruas = RegServicioGrua.objects.all()
    reg_tipo_plan = RegTipoPlan.objects.all()
    reg_presupuestos_liquidador = RegPresupuesto.objects.all()

    context = {'reg_asegurados': reg_asegurados, 'reg_vehiculos': reg_vehiculos, 'reg_polizas': reg_polizas,
               'reg_siniestros': reg_siniestros, 'reg_talleres': reg_talleres, 'reg_usuarios': reg_usuarios,
               'reg_actas_recepcion': reg_actas_recepcion, 'reg_actas_retiro': reg_actas_retiro,
               'reg_actas_rechazo': reg_actas_rechazo,
               'reg_informes': reg_informes, 'reg_presupuestos': reg_presupuestos,
               'reg_siniestros_taller': reg_siniestros_taller,
               'reg_gruas': reg_gruas, 'reg_servicio_gruas': reg_servicio_gruas, 'reg_tipo_plan': reg_tipo_plan,
               'reg_presupuestos_liquidador': reg_presupuestos_liquidador}

    return render(request, 'dashboard/home.html', context)


def UpdateSiniestroFotos(request, id):
    siniestro = get_object_or_404(Siniestro, id=id)
    if request.method == 'POST':
        form = SiniestroFotosUpdate(
            request.POST, request.FILES, instance=siniestro)
        if form.is_valid():
            form.save()
            return redirect('asegurado_consulta')
    else:
        form = SiniestroFotosUpdate(instance=siniestro)
    return render(request, 'dashboard/asegurados/asegurado_fotos.html', {
        'form': form
    })


@login_required(login_url='login')
def FotoSiniestroView(request, id):
    siniestro = get_object_or_404(Siniestro, id=id)
    siniestros = Siniestro.objects.filter(id=siniestro.id).order_by('id')
    context = {'siniestros': siniestros}
    return render(request, 'dashboard/siniestro_detail.html', context)


def consultaSiniestroDetalleView(request, pk):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT S.ID,A.RUT_ASEGURADO,A.PRIMER_NOMBRE,A.PRIMER_APELLIDO,S.POLIZA_ID_POLIZA,S.FECHA_HR,S.DESCRIPCION,X.NOMBRE,S.EST_SINIESTRO_ID_EST_SINIESTRO,S.DIRECCION,V.NOMBRE,S.GRUA_PATENTE_GRUA,T.NOMBRE,T.TELEFONO,T.CORREO,T.DIRECCION,C.NOMBRE FROM DASHBOARD_SINIESTRO S JOIN DASHBOARD_TALLER T ON (S.TALLER_ID_TALLER=T.ID) JOIN DASHBOARD_COMUNA C ON (T.COMUNA_ID_COMUNA=C.ID) JOIN DASHBOARD_TIPOACCIDENTE X ON(S.TIPO_ACCIDENTE_ID_TIPO_ACC=X.ID) JOIN DASHBOARD_ASEGURADO A ON(S.ASEGURADO_RUT_ASEGURADO=A.RUT_ASEGURADO)  JOIN DASHBOARD_COMUNA V ON (S.COMUNA_ID_COMUNA=V.ID) WHERE (S.ID=" + pk + ")")
        dato = cursor.fetchall()
        dato = list(dato)
        print(dato)
    return render(request, 'dashboard/asegurados/asegurado_consulta_detalle.html', {'dato': dato})


def siniestroDetallePdf(request, pk):
    options = {
        'page-size': 'Letter',
        'margin-top': '0.5in',
        'margin-right': '1in',
        'margin-bottom': '0.5in',
        'margin-left': '1in',
        'encoding': "UTF-8",
    }

    path_wkthmltopdf = b'C:\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url('http://127.0.0.1:8000/consultaSiniestroDetalleView/' +
                          str(pk), False, options=options, configuration=config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="DetalleSiniestro.pdf" '
    return response


# todo Crear Modulo y CRUD de Servicios Grua
@login_required(login_url='login')
def ServicioGruaView(request):
    servicios_gruas = ServicioGrua.objects.all().exclude(estado=False).order_by('id')
    context = {'servicios_gruas': servicios_gruas}
    return render(request, 'dashboard/servicioGrua/servicio_grua.html', context)


@login_required(login_url='login')
def ServicioGruaInactivos(request):
    servicios_gruas_disabled = ServicioGrua.objects.filter(estado=False)
    context = {'servicios_gruas_disabled': servicios_gruas_disabled}
    return render(request, 'dashboard/servicioGrua/servicio_grua_disabled.html', context)


def SaveAllServicios(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            servicios_gruas = ServicioGrua.objects.all().exclude(estado=False).order_by('id')
            context = {'servicios_gruas': servicios_gruas}
            data['servicios_gruas'] = render_to_string(
                'dashboard/servicioGrua/servicio_grua_2.html', context)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


# Read
@login_required(login_url='login')
def ServicioGruaCreate(request):
    if request.method == 'POST':
        form = ServicioGruaForm(request.POST)
        servicio_grua = form.save(commit=False)
        servicio_grua.usuario_rut_usuario = request.user
    else:
        form = ServicioGruaForm()
    return SaveAllServicios(request, form, 'dashboard/servicioGrua/servicio_grua_create.html')

@staff_member_required(login_url='login')
def ServicioGruaUpdate(request, id):
    servicio_grua = get_object_or_404(ServicioGrua, id=id)
    if request.method == 'POST':
        form = ServicioGruaForm(request.POST, instance=servicio_grua)
        servicio = form.save(commit=False)
        servicio.usuario_rut_usuario = request.user
    else:
        form = ServicioGruaForm(instance=servicio_grua)
    return SaveAllServicios(request, form, 'dashboard/servicioGrua/servicio_grua_update.html')
