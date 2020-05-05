from django import forms
from .models import Poliza, Asegurado, Vehiculo, Siniestro, Taller


# FORMULARIO POLIZA
class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = [
            'id',
            'vigente',
            'fecha_inicio',
            'fecha_fin',
            'asegurado_rut_asegurado',
            'vehiculo_patente_vehiculo',
        ]
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'vigente': forms.HiddenInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa estado vigencia'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut asegurado'}),
            'vehiculo_patente_vehiculo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente vehículo'})
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
            'usuario_rut_usuario'
        ]
        widgets = {
            'rut_asegurado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su rut', 'pattern': '^[0-9]{8,9}[-|‐]{1}[0-9kK]{1}$'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su primer nombre', 'pattern': '[A-Za-z]+'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su segundo nombre', 'pattern': '[A-Za-z]+'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su primer apellido', 'pattern': '[A-Za-z]+'}),
            'segundo_apeliido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su segundo apellido', 'pattern': '[A-Za-z]+'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su correo', 'type': 'email', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su teléfono', 'min': '9'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'usuario_rut_usuario': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut usuario'}),
        }

    def clean(self):
        primer_nombre = self.cleaned_data.get('primer_nombre')
        print("holi")
        if len(primer_nombre) < 3:
            self._errors['primer_nombre'] = self.error_class([
                'Minimo de 3 caracteres'
            ])
        return self.cleaned_data

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
    class Meta:
        model = Siniestro
        fields = ['id', 'fecha_hr', 'descripcion', 'parte_policial', 'foto_licencia', 'tipo_accidente_id_tipo_acc',
                  'est_siniestro_id_est_siniestro', 'taller_id_taller', 'grua_patente_grua', 'usuario_rut_usuario', 'poliza_id_poliza']
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'fecha_hr': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'required form-control', 'placeholder': 'Ingrea una descripción'}),
            'parte_policial': forms.FileInput(attrs={'class': 'form-control'}),
            'foto_licencia': forms.FileInput(attrs={'class': 'form-control'}),
            'tipo_accidente_id_tipo_acc': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa tipo accidente'}),
            'est_siniestro_id_est_siniestro': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa estado siniestro'}),
            'taller_id_taller': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa id taller'}),
            'grua_patente_grua': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente grúa'}),
            'usuario_rut_usuario': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa rut asegurado'}),
            'poliza_id_poliza': forms.Select(attrs={'class': 'required form-control', 'placeholder': 'Ingresa id póliza'}),
        }


# FORMULARIO BORRADO LOGICO SINIESTRO


class DeshabilitarSiniestroForm(forms.ModelForm):

    class Meta:
        model = Siniestro
        fields = ['est_siniestro_id_est_siniestro']
        widgets = {
            'est_siniestro_id_est_siniestro': forms.HiddenInput(attrs={'class': 'required form-control',  'id': 'est_siniestro_id_est_siniestro_siniestro'}),
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
            'asegurado_rut_asegurado'
        ]
        widgets = {
            'patente_vehiculo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa año (YYYY)'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa modelo'}),
            'nro_motor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su número del motor'}),
            'tipo_vehiculo_id_tipo_auto': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa tipo de vehículo'}),
            'marca_id_marca': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa marca'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut usuario'}),
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
            'estado',
            # 'estado_delete',
            'usuario_rut_usuario',
        ]
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa nombre'}),
            'razon_social': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa razón social'}),
            'telefono': forms.NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa número de teléfono', 'min' : '9'}),
            'correo': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa correo', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'}),
            'capacidad_taller': forms.NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa capacidad máxima'}),
            'estado': forms.TextInput(
                attrs={'class': 'required form-control', 'placeholder': 'Ingresa estado taller'}),
            # 'estado_delete': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'usuario_rut_usuario': forms.Select(attrs={'class': 'required form-control'}),
        }


class DeshabilitarTallerForm(forms.ModelForm):

    class Meta:
        model = Taller
        fields = ['estado_delete']
        widgets = {
            'estado_delete': forms.HiddenInput(attrs={'class': 'required form-control', 'id': 'estado_delete_taller'}),
        }
