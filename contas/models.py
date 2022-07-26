from distutils.command.upload import upload
from pickle import NONE
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    foto_perfil = models.ImageField(upload_to="fotos_de_perfil")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    biografia = models.CharField(max_length=160, blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True, null=True)
    birt_date = models.DateField(auto_now=False, blank=True, null=True)


