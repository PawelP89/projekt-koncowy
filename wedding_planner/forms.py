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
    wearf = forms.DecimalField(label='Suknia', decimal_places=2)
    wearm = forms.DecimalField(label='Garnitur', decimal_places=2)
    quantity = forms.DecimalField(label='Liczba gości', decimal_places=2)
    plate_price = forms.DecimalField(label='Cena za talerzyk', decimal_places=2)
    music = forms.DecimalField(label='dj/zespół', decimal_places=2)
    movie = forms.DecimalField(label='Ekipa filmowa', decimal_places=2)
    photo = forms.DecimalField(label='Fotograf', decimal_places=2)



class BForm(forms.Form):
    wearf = forms.DecimalField(label='Suknia', decimal_places=2)
    wearm = forms.DecimalField(label='Garnitur', decimal_places=2)
    quantity = forms.DecimalField(label='Liczba gości', decimal_places=2)
    plate_price = forms.DecimalField(label='Cena za talerzyk', decimal_places=2)
    music = forms.DecimalField(label='dj/zespół', decimal_places=2)
    movie = forms.DecimalField(label='Ekipa filmowa', decimal_places=2)
    photo = forms.DecimalField(label='Fotograf', decimal_places=2)


class CForm(forms.Form):
    wearf = forms.DecimalField(label='Suknia', decimal_places=2)
    wearm = forms.DecimalField(label='Garnitur', decimal_places=2)
    quantity = forms.DecimalField(label='Liczba gości', decimal_places=2)
    plate_price = forms.DecimalField(label='Cena za talerzyk', decimal_places=2)
    music = forms.DecimalField(label='dj/zespół', decimal_places=2)
    movie = forms.DecimalField(label='Ekipa filmowa', decimal_places=2)
    photo = forms.DecimalField(label='Fotograf', decimal_places=2)