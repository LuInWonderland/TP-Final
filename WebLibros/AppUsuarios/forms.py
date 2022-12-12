from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(label = 'Nombre')
    last_name = forms.CharField(label = 'Apellido')
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repetir contraseña', widget = forms.PasswordInput)

    class Meta:
        model = User
        help_texts = {
            'password ': (''),
        }
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

    