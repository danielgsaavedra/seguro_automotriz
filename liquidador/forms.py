from django import forms
from dashboard.models import TipoPlan, Presupuesto


class TipoPlanForm(forms.ModelForm):
    class Meta:
        model = TipoPlan
        fields = [
            'id',
            'nombre',
            'valor',
            'deducible',
            'cobertura_max',
            'descripcion',
            'garantia',
        ]
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Ingresa nombre',
                                             'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'nombre_tipo'}),
            'valor': forms.TextInput(
                attrs={'class': 'required form-control', 'placeholder': 'Ingresa valor', 'id': 'valor_tipo_plan',
                       'onkeypress': 'return soloNumeros(event)', 'onKeyUp': 'pierdeFoco(this)'}),
            'deducible': forms.TextInput(
                attrs={'class': 'required form-control', 'placeholder': 'Ingresa deducible', 'id': 'deducible',
                       'pattern': '[0-9]{1,}',
                       'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'}),
            'cobertura_max': forms.TextInput(
                attrs={'class': 'required form-control', 'placeholder': 'Ingresa cobertura max', 'id': 'cobertura',
                       'onkeypress': 'return soloNumeros(event)', 'onKeyUp': 'pierdeFoco(this)'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'required form-control', 'placeholder': 'Ingresa descripción de tipo de plan',
                       'id': 'descripcion'}),
            'garantia': forms.CheckboxInput(attrs={'class': 'form-control'}),

        }

class DeshabilitarTipoPlanForm(forms.ModelForm):
    class Meta:
        model = TipoPlan
        fields = ['estado']
        widgets = {
            'estado': forms.HiddenInput(attrs={'class': 'required form-control', 'id': 'estado_tipo'}),
        }


class AproRechPresupuestoForm(forms.ModelForm):
    class Meta:
        model = Presupuesto
        fields = ['estado_id_est_presupuesto']
        widgets = {
            'estado_id_est_presupuesto': forms.HiddenInput(
                attrs={'class': 'required form-control', 'id': 'estado_id_est_presupuesto'}),
        }
