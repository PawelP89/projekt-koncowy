from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import ListaForm, CreateUserForm
from wedding_planner.models import Lista
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse
import random

# Create your views here.


class HomePage(View):
    def get(self, request):
        return render(request, "homePage.html")


class FrontPage(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'front'

    def get(self, request):
        return render(request, "frontPage.html")


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Witaj {username}! Konto zostało utworzone pomyślnie!')
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, "register.html", {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')


class OptionA(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'front'

    def get(self, request):
        form = ListaForm()
        ctx = {"form": form}
        return render(request, 'optiona.html', ctx)

    def post(self, request):
        form = ListaForm(request.POST or None, request.FILES or None)
        ctx = {"form": form}

        if form.is_valid():
            form.save()
            return redirect('podsumowanie')
        return render(request, "optiona", ctx)


class Kontakt(View):
    def get(self, request):
        return render(request, 'kontakt.html')

class Onas(View):
    def get(self, request):
        return render(request, 'onas.html')

class Relacje(View):
    def get(self, request):
        return render(request, 'relacje.html')


class Podsumowanie(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'front'

    def get(self, request):
        lista = Lista.objects.all().order_by('-id')
        ctx = {
            "lista": lista
        }
        return render(request, "podsumowanie.html", ctx)


