from django import forms
from dashboard.models import Usuario

class UsuarioRegisterForm(forms.ModelForm):

    password1 = forms.CharField(widget= forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Ingresa contraseña',
            'id':'password1',
            'required':'required',}
    ))

    password2 = forms.CharField(widget= forms.PasswordInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Ingresa nuevamente contraseña',
            'id':'password2',
            'required':'required',}
    ))

    class Meta:
        model = Usuario
        fields = [
            'rut_usuario',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'email',
            'telefono',
            'rol'
        ]
        widgets = {
            'rut_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa RUT '}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer nombre'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo nombre'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer apellido'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa correo'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa telefono'}),
            'rol': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ingresa un rol'}),
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(self.cleaned_data)
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
    
    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
