from distutils.command.upload import upload
from pickle import NONE
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    foto_perfil = models.ImageField(upload_to="fotos_de_perfil")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

