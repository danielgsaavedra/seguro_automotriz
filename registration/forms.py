from django import forms
from dashboard.models import Usuario, Taller


class UsuarioRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioRegisterForm, self).__init__(*args, **kwargs)
        self.fields['taller_id_taller'].queryset = Taller.objects.filter(
            estado=1)

    password1 = forms.CharField(max_length=12, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa contraseña',
            'id': 'password1',
            'required': 'required',
            'pattern': '^[a-zA-Z0-9._%+-]{5,}'
        }
    ))

    password2 = forms.CharField(max_length=12, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa nuevamente contraseña',
            'id': 'password2',
            'required': 'required', }
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
            'rol',
            'taller_id_taller'
        ]
        widgets = {
            'rut_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa RUT', 'pattern': '^[0-9]{8,9}[-|‐]{1}[0-9kK]{1}$', 'oninput': 'checkRut(this)'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_nombre_usuario'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_nombre_usuario'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_apellido_usuario'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_apellido_usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa correo', 'type': 'email', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 'id': 'email_usuario'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa teléfono', 'pattern': '[0-9]{9,}', 'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)', 'id': 'telefono_usuario'}),
            'rol': forms.Select(attrs={'class': 'form-control', 'id': 'rol_usuario', 'onchange': 'seleccionarTaller()'}),
            'taller_id_taller': forms.Select(attrs={'class': 'form-control', 'id': 'id_taller', 'disabled': 'true'}),

        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(self.cleaned_data)
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UsuarioFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioFormUpdate, self).__init__(*args, **kwargs)
        self.fields['taller_id_taller'].queryset = Taller.objects.filter(
            estado=1)

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
            'rol',
            'taller_id_taller'
        ]
        widgets = {
            'rut_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa RUT ', 'pattern': '^[0-9]{8,9}[-|‐]{1}[0-9kK]{1}$', 'oninput': 'checkRut(this)', 'disabled': 'true'}),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_nombre_usuario'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo nombre', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_nombre_usuario'}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa primer apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 'p_apellido_usuario'}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa segundo apellido', 'pattern': '[A-Za-zÀ-ÿ\u00f1\u00d1 ]{3,}', 'id': 's_apellido_usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa correo', 'type': 'email', 'pattern': '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', 'id': 'email_usuario'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa teléfono', 'pattern': '[0-9]{9,}', 'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)', 'id': 'telefono_usuario'}),
            'rol': forms.Select(attrs={'class': 'form-control', 'id': 'rol_usuario', 'onchange': 'seleccionarTaller()'}),
            'taller_id_taller': forms.Select(attrs={'class': 'form-control', 'id': 'id_taller', 'disabled': 'true'}),

        }


class DeshabilitarUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['is_active']
        widgets = {
            'is_active': forms.HiddenInput(attrs={'class': 'required form-control', 'id': 'estado_usuario'}),
        }
