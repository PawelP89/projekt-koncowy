from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class AForm(forms.Form):
    quantity = forms.CharField(label='Liczba gości', max_length=100)

class BForm(forms.Form):
    quantity = forms.CharField(label='Liczba gości', max_length=100)

class CForm(forms.Form):
    quantity = forms.CharField(label='Liczba gości', max_length=100)