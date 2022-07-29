from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='opcoes')),
    path('opcoes/', views.pagina_inicial, name='opcoes'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout, name='logout'),
    path('auth/', include('django.contrib.auth.urls')),
    path('perfil', views.profile, name='profile'),
]
