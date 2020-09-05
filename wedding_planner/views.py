from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import AForm, BForm, CForm, CreateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse

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
            return redirect('login')

    ctx = {'form': form}
    return render(request, "register.html", ctx)




class OptionA(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'front'
    def get(self, request):
        form = AForm()
        return render(request, 'optiona.html', {'form': form})
    def post(self, request):
        form = AForm(request.POST)
        if form:
            return redirect('podsumowanie')

class OptionB(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'front'

    def get(self, request):
        form = BForm()
        return render(request, 'optionb.html', {'form': form})

    def post(self, request):
        form = AForm(request.POST)
        if form:
            return HttpResponseRedirect('/thanks/')


class OptionC(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'front'

    def get(self, request):
        form = CForm()
        return render(request, 'optionc.html', {'form': form})

    def post(self, request):
        form = AForm(request.POST)
        if form.quantity < 50:
            return redirect('/thanks/')

class Kontakt(View):
    def get(self, request):
        return render(request, 'kontakt.html')

class Onas(View):
    def get(self, request):
        return render(request, 'onas.html')

class Relacje(View):
    def get(self, request):
        return render(request, 'relacje.html')

class Podsumowanie(View):
    def get(self, request):
        return render(request, "podsumowanie.html")
