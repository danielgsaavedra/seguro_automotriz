from django import forms
from .models import Poliza, Asegurado


class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['id_poliza', 'vigente',
                  'fecha_inicio', 'fecha_fin', 'firma', 'asegurado_rut_asegurado', 'vehiculo_patente_vehiculo']
        widgets = {
            'id_poliza': forms.NumberInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa ID póliza'}),
            'vigente': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa estado vigencia'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'required form-control', 'type': 'date'}),
            'firma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa firma'}),
            'asegurado_rut_asegurado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut asegurado'}),
            'vehiculo_patente_vehiculo': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa patente vehículo'})
        }


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
            'rut_asegurado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su rut'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su primer nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su segundo nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su primer apellido'}),
            'segundo_apeliido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su segundo apellido'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su correo'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su teléfono'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'usuario_rut_usuario': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa rut usuario'}),
        }
