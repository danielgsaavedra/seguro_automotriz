from django import forms
from dashboard.models import Siniestro, FormularioActa

class ActasForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(SiniestroForm, self).__init__(*args, **kwargs)
    #     self.fields['taller_id_taller'].queryset = Taller.objects.filter(estado=1)
    class Meta:
        model = FormularioActa
        fields = ['id', 'observaciones', 'siniestro_id', 'taller_id_taller',
                   'tipo_acta_id_tipo_acta', 'usuario_rut_usuario']
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'required form-control', 'placeholder': 'Ingrea observaciones'}),
            'siniestro_id': forms.Select(attrs={'class': 'form-control'}),
            'taller_id_taller': forms.Select(attrs={'class': 'form-control'}),
            'tipo_acta_id_tipo_acta': forms.Select(attrs={'class': 'required form-control'}),
            'usuario_rut_usuario': forms.Select(attrs={'class': 'required form-control'}),
        }