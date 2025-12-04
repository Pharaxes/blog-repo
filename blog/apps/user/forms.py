from django.contrib.auth.forms import AuthenticationForm
from django import forms


class RegisterForm():
    pass


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'bg-blue-50', 'placeholder': 'Usuario'}
    ))

    password = forms.CharField(max_length=150, widget=forms.PasswordInput(
        attrs={'class': 'bg-red-50', 'placeholder': 'Contraseña'}
    ))