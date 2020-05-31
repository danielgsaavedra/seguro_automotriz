from django import forms
from dashboard.models import Siniestro, FormularioActa


class ActasForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(SiniestroForm, self).__init__(*args, **kwargs)
    #     self.fields['taller_id_taller'].queryset = Taller.objects.filter(estado=1)
    class Meta:
        model = FormularioActa
        fields = ['id', 'observaciones']
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'required form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'required form-control', 'placeholder': 'Ingresa observaciones', 'id': 'observaciones', 'required': 'True'}),
        }
