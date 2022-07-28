from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='opcoes')),
    path('opcoes/', views.pagina_inicial, name='opcoes'),
    path('registro/', views.registro, name='registro'),
    path('auth/', include('django.contrib.auth.urls')),
    path('perfil', views.profile, name='profile'),  


]
