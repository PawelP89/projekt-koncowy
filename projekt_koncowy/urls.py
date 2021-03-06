"""projekt_koncowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from wedding_planner.views import HomePage, FrontPage, OptionA, \
    Kontakt, Onas, Relacje, registerPage, Podsumowanie, Profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerPage),
    path('profile/', Profile.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', HomePage.as_view(), name='home'),
    path('front/', FrontPage.as_view(), name='front'),
    path('optiona/', OptionA.as_view()),
    path('kontakt/', Kontakt.as_view()),
    path('onas/', Onas.as_view()),
    path('relacje/', Relacje.as_view()),
    path('podsumowanie/', Podsumowanie.as_view(), name='podsumowanie'),

]
