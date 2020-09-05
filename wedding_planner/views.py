from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import AForm, BForm, CForm, CreateUserForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse

# Create your views here.

class HomePage(View):
    def get(self, request):
        return render(request, "homePage.html")

class FrontPage(View):
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



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    def post(self, request):
        form = LoginForm(request.POST)
        ctx = {"form": form}
        if form.is_valid():
            if (form.cleaned_data["login"] == "root" and
                    form.cleaned_data["password"] == "very_secret"):
                return redirect("front")
        return render(request, "login.html", ctx)

class OptionA(View):
    def get(self, request):
        form = AForm()
        return render(request, 'optiona.html', {'form': form})
    def post(self, request):
        form = AForm(request.POST)
        if form:
            return HttpResponseRedirect('/thanks/')

class OptionB(View):
    def get(self, request):
        form = BForm()
        return render(request, 'optionb.html', {'form': form})
    def post(self, request):
        form = AForm(request.POST)
        if form:
            return HttpResponseRedirect('/thanks/')

class OptionC(View):
    def get(self, request):
        form = CForm()
        return render(request, 'optionc.html', {'form': form})
    def post(self, request):
        form = AForm(request.POST)
        if form:
            return HttpResponseRedirect('/thanks/')

class Kontakt(View):
    def get(self, request):
        return render(request, 'kontakt.html')

class Onas(View):
    def get(self, request):
        return render(request, 'onas.html')

class Relacje(View):
    def get(self, request):
        return render(request, 'relacje.html')
