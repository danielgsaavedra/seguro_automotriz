from django import forms
from .models import Poliza, Asegurado, Vehiculo, Siniestro, Taller, Grua


# FORMULARIO POLIZA
class PolizaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PolizaForm, self).__init__(*args, **kwargs)
        self.fields['asegurado_rut_asegurado'].queryset = Asegurado.objects.filter(
            estado=1)

    class Meta:
        model = Poliza
        fields = [
            'id',
            'vigente',
            'fecha_inicio',
            'fecha_fin',
            'asegurado_rut_asegurado',
            'vehiculo_patente_vehiculo',
            'tipo_plan_id_tip_plan',
        ]
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'vigente': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'required form-control', 'id': 'fecha_inicio', 'readonly': 'False'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'required form-control', 'id': 'fecha_fin', 'placeholder': 'Ingresa fecha de termino'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'form-control', 'onchange': "cargarPatentes();", 'id': 'poli_rut_asegurado'}),
            'vehiculo_patente_vehiculo': forms.Select(attrs={'class': 'form-control', 'id': 'poli_patente', 'disabled': 'true'}),
            'tipo_plan_id_tip_plan': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_plan'})
        }


class PolizaFormUpdate(forms.ModelForm):

    class Meta:
        model = Poliza
        fields = [
            'id',
            'vigente',
            'fecha_inicio',
            'fecha_fin',
            'asegurado_rut_asegurado',
            'vehiculo_patente_vehiculo',
            'tipo_plan_id_tip_plan',
        ]
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'vigente': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'required form-control', 'id': 'fecha_inicio', 'readonly': 'False'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'required form-control', 'id': 'fecha_fin', 'placeholder': 'Ingresa fecha de termino'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'form-control', 'onchange': "cargarPatentes();", 'id': 'poli_rut_asegurado', 'disabled': 'true'}),
            'vehiculo_patente_vehiculo': forms.Select(attrs={'class': 'form-control', 'id': 'poli_patente', 'disabled': 'true'}),
            'tipo_plan_id_tip_plan': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_plan', 'disabled': 'true'})
        }

# FORMULARIO BORRADO LOGICO POLIZA


class DeshabilitarPolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['estado']
        widgets = {
            'estado': forms.HiddenInput(attrs={'class': 'required form-control', 'id': 'estado_poliza'}),
        }


# FORMULARIO ASEGURADO


class AseguradoForm(forms.ModelForm):
    class Meta:
        model = Asegurado
        fields = [
            'rut_asegurado',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apeliido',
            'correo',
            'telefono',
            'fecha_nacimiento',
            'direccion',
            'comuna_id_comuna',
        ]
        widgets = {
            'rut_asegurado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa RUT', 'pattern': '^[0-9]{7,9}[-|‐]{1}[0-9kK]{1}$', 'oninput': 'checkRut(this)'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_nombre_asegurado'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_nombre_asegurado'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_apellido_asegurado'}),
            'segundo_apeliido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_apellido_asegurado'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa correo', 'type': 'email', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 'id': 'correo_asegurado'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa teléfono', 'pattern': '[0-9]{9,}', 'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)', 'id': 'telefono_asegurado'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'fecha_asegurado'}),
            'direccion': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa dirección','id': 'direccion_asegurado', 'pattern': '[A-Za-zÀ-ÿ0-9 ]{4,}'}),
            'comuna_id_comuna': forms.Select(attrs={'class': 'required form-control', 'id': 'comuna_asegurado'}),
        }

    def clean_rut_asegurado(self):
        rut_asegurado = self.cleaned_data.get("rut_asegurado")
        if Asegurado.objects.filter(rut_asegurado=rut_asegurado).exists():
            raise forms.ValidationError(
                "El RUT ya esta registrado, prueba con otro")
        return rut_asegurado


class AseguradoFormUpdate(forms.ModelForm):
    class Meta:
        model = Asegurado
        fields = [
            'rut_asegurado',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apeliido',
            'correo',
            'telefono',
            'fecha_nacimiento',
            'direccion',
            'comuna_id_comuna',
        ]
        widgets = {
            'rut_asegurado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa RUT', 'pattern': '^[0-9]{7,9}[-|‐]{1}[0-9kK]{1}$', 'oninput': 'checkRut(this)', 'disabled': 'true'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_nombre_asegurado'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_nombre_asegurado'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_apellido_asegurado'}),
            'segundo_apeliido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_apellido_asegurado'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa correo', 'type': 'email', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 'id': 'correo_asegurado'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa teléfono', 'pattern': '[0-9]{9,}', 'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)', 'id': 'telefono_asegurado'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'fecha_asegurado'}),
            'direccion': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa dirección','id': 'direccion_asegurado', 'pattern': '[A-Za-zÀ-ÿ0-9 ]{4,}'}),
            'comuna_id_comuna': forms.Select(attrs={'class': 'required form-control', 'id': 'comuna_asegurado'}),
        }

# FORMULARIO BORRADO LOGICO ASEGURADO


class DeshabilitarAseguradoForm(forms.ModelForm):
    class Meta:
        model = Asegurado
        fields = ['estado']
        widgets = {
            'estado': forms.HiddenInput(attrs={'class': 'required form-control', 'id': 'estado_asegurado'}),
        }


# FORMULARIO  SINIESTROS


class SiniestroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SiniestroForm, self).__init__(*args, **kwargs)
        self.fields['taller_id_taller'].queryset = Taller.objects.filter(
            estado=1)
        self.fields['grua_patente_grua'].queryset = Grua.objects.filter(
            estado=1)
        self.fields['asegurado_rut_asegurado'].queryset = Asegurado.objects.filter(
            estado=1)
        self.fields['poliza_id_poliza'].queryset = Poliza.objects.filter(
            vigente=1)

    class Meta:
        model = Siniestro
        fields = ['id', 'descripcion', 'parte_policial', 'foto_licencia', 'tipo_accidente_id_tipo_acc',
                  'taller_id_taller', 'grua_patente_grua', 'poliza_id_poliza', 'asegurado_rut_asegurado', 'direccion',
                  'comuna_id_comuna']
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control', 'name': 'id_siniestro'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'required form-control', 'placeholder': 'Ingrea una descripción', 'id': 'descripcion'}),
            'parte_policial': forms.FileInput(attrs={'class': 'form-control'}),
            'foto_licencia': forms.FileInput(attrs={'class': 'form-control'}),
            'tipo_accidente_id_tipo_acc': forms.Select(
                attrs={'class': 'required form-control', 'id': 'tipo_accidente'}),
            'taller_id_taller': forms.Select(
                attrs={'class': 'required form-control', 'id': 'taller', 'name': 'taller_id_taller'}),
            'grua_patente_grua': forms.Select(attrs={'class': 'form-control'}),
            'poliza_id_poliza': forms.Select(
                attrs={'class': 'required form-control', 'id': 'poliza', 'disabled': 'true',
                       'name': 'poliza_id_poliza'}),
            'asegurado_rut_asegurado': forms.Select(
                attrs={'class': 'required form-control', 'id': 'asegurado_rut', 'onchange': "cargarPoliza();",
                       'name': 'asegurado_rut_asegurado'}),
            'direccion': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa dirección',
                                                'pattern': '^[a-zA-Z0-9._%+- ]{4,}', 'id': 'direccion'}),
            'comuna_id_comuna': forms.Select(
                attrs={'class': 'required form-control', 'id': 'comuna', 'name': 'comuna_id_comuna'})
        }


class SiniestroFormUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SiniestroFormUpdate, self).__init__(*args, **kwargs)
        self.fields['taller_id_taller'].queryset = Taller.objects.filter(
            estado=1)
        self.fields['grua_patente_grua'].queryset = Grua.objects.filter(
            estado=1)

    class Meta:
        model = Siniestro
        fields = ['id', 'descripcion', 'parte_policial', 'foto_licencia', 'tipo_accidente_id_tipo_acc',
                  'taller_id_taller', 'grua_patente_grua', 'poliza_id_poliza', 'asegurado_rut_asegurado', 'direccion', 'comuna_id_comuna']
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'required form-control', 'placeholder': 'Ingrea una descripción', 'id': 'descripcion'}),
            'parte_policial': forms.FileInput(attrs={'class': 'form-control'}),
            'foto_licencia': forms.FileInput(attrs={'class': 'form-control'}),
            'tipo_accidente_id_tipo_acc': forms.Select(attrs={'class': 'required form-control', 'id': 'tipo_accidente', 'disabled': 'true'}),
            'taller_id_taller': forms.Select(attrs={'class': 'required form-control', 'id': 'taller'}),
            'grua_patente_grua': forms.Select(attrs={'class': 'form-control'}),
            'poliza_id_poliza': forms.Select(attrs={'class': 'required form-control', 'id': 'poliza', 'disabled': 'true'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'required form-control', 'id': 'asegurado_rut', 'onchange': "cargarPoliza();", 'disabled': 'true'}),
            'direccion': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa dirección',
                                                'pattern': '^[a-zA-Z0-9._%+- ]{4,}', 'id': 'direccion', 'disabled': 'true' }),
            'comuna_id_comuna': forms.Select(
                attrs={'class': 'required form-control', 'id': 'comuna', 'name': 'comuna_id_comuna', 'disabled': 'true'})
        }


class SiniestroFotosUpdate(forms.ModelForm):
    class Meta:
        model = Siniestro
        fields = ['parte_policial', 'foto_licencia']
        widgets = {
            'parte_policial': forms.FileInput(attrs={'class': 'form-control', 'id': 'parte_poli'}),
            'foto_licencia': forms.FileInput(attrs={'class': 'form-control', 'required': 'true', 'id': 'licencia'}),
        }

# FORMULARIO BORRADO LOGICO SINIESTRO


class DeshabilitarSiniestroForm(forms.ModelForm):
    class Meta:
        model = Siniestro
        fields = ['est_siniestro_id_est_siniestro']
        widgets = {
            'est_siniestro_id_est_siniestro': forms.HiddenInput(
                attrs={'class': 'required form-control', 'id': 'est_siniestro_id_est_siniestro_siniestro'}),
        }


# FORMULARIO VEHICULO


class VehiculoForm(forms.ModelForm):

    class Meta:

        model = Vehiculo
        fields = [
            'patente_vehiculo',
            'anio',
            'modelo',
            'nro_motor',
            'tipo_vehiculo_id_tipo_auto',
            'marca_id_marca',
        ]
        widgets = {
            'patente_vehiculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente', 'id': 'patente', 'pattern': '^[a-zA-Z0-9._%+-]{8,}'}),
            'anio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa año (YYYY)', 'pattern': '[0-9]{4,}', 'id': 'anio', 'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa modelo', 'id': 'modelo', 'pattern': '^[a-zA-Z0-9._%+- ]{4,}'}),
            'nro_motor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su número del motor', 'id': 'motor', 'pattern': '^[a-zA-Z0-9._%+- ]{4,}'}),
            'tipo_vehiculo_id_tipo_auto': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_vehi'}),
            'marca_id_marca': forms.Select(attrs={'class': 'form-control', 'id': 'marca_vehi'}),
        }


class VehiculoFormUpdate(forms.ModelForm):

    class Meta:

        model = Vehiculo
        fields = [
            'patente_vehiculo',
            'anio',
            'modelo',
            'nro_motor',
            'tipo_vehiculo_id_tipo_auto',
            'marca_id_marca',
            'asegurado_rut_asegurado'
        ]
        widgets = {
            'patente_vehiculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente', 'id': 'patente', 'pattern': '^[a-zA-Z0-9._%+-]{8,}', 'disabled': 'true'}),
            'anio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa año (YYYY)', 'pattern': '[0-9]{4,}', 'id': 'anio', 'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa modelo', 'id': 'modelo', 'pattern': '^[a-zA-Z0-9._%+- ]{4,}'}),
            'nro_motor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su número del motor', 'id': 'motor', 'pattern': '^[a-zA-Z0-9._%+- ]{4,}'}),
            'tipo_vehiculo_id_tipo_auto': forms.Select(attrs={'class': 'form-control', 'id': 'tipo_vehi'}),
            'marca_id_marca': forms.Select(attrs={'class': 'form-control', 'id': 'marca_vehi'}),
            'asegurado_rut_asegurado': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'rut_asegurado_vehi'}),
        }


class TallerForm(forms.ModelForm):

    class Meta:
        model = Taller
        fields = [
            'id',
            'nombre',
            'razon_social',
            'telefono',
            'correo',
            'capacidad_taller',
            'direccion',
            'comuna_id_comuna'

        ]
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'nombre_taller'}),
            'razon_social': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa razón social', 'pattern': '[A-Za-zÀ-ÿ0-9 ]{4,}', 'id': 'razon_social'}),
            'telefono': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa número de teléfono', 'pattern': '[0-9]{9,}', 'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)', 'id': 'telefono_taller'}),
            'correo': forms.TextInput(attrs={'class': 'required form-control', 'type': 'email', 'placeholder': 'Ingresa correo', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 'id': 'correo_taller'}),
            'capacidad_taller': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa capacidad máxima', 'id': 'capacidad', 'onkeypress': 'return soloNumeros(event)', 'onKeyUp': 'pierdeFoco(this)'}),
            'direccion': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa dirección', 'pattern': '^[a-zA-Z0-9._%+- ]{4,}', 'id': 'direccion'}),
            'comuna_id_comuna': forms.Select(attrs={'class': 'required form-control', 'id': 'comuna', 'name': 'comuna_id_comuna'})
        }


class DeshabilitarTallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ['estado_delete']
        widgets = {
            'estado_delete': forms.HiddenInput(attrs={'class': 'required form-control', 'id': 'estado_delete_taller'}),
        }
