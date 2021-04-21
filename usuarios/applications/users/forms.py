from django import forms
from django.contrib.auth import authenticate
from .models import Usuario

class UserRegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(
        label="contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label="contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'repetir contraseña'
            }
        )
    )

    class Meta:
        model = Usuario
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    """
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            print(self.cleaned_data['password1'], self.cleaned_data['password2'])
            self.add_error('password2','Las contraseña no son las mismas')

    implementar que una contraseña solo admita
    una contraseña mayor a 5 digitos
    """ 
    def clean(self):
        cleaned_data = super(UserRegisterForm,self).clean()
        password = cleaned_data.get('password1')
        confirm = cleaned_data.get('password2')
        
        if len(password) <= 4:
            self.add_error('password1','Debe de tener al menos 5 caracteres')
        
        elif password != confirm:
            self.add_error('password2','Las contraseñas NO son iguales')

class LoginForm(forms.Form):
    username = forms.CharField(
        label="username",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'style':'{margin 10px}'
            }
        )
    )
    password = forms.CharField(
        label="contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña'
            }
        )
    )

    def clean(self): #cuando no sabemos a que campo hacer la validacion solo se pone clean
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Los datos de tu usuario no son correctos')

        return self.cleaned_data


