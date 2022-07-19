from pickle import NONE
from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.NOT_PROVIDED)
    date = models.DateTimeField(auto_now_add=True)
    texto = models.CharField(max_length=200,blank=True)

class Noticias(models.Model):
    autor = models.CharField(max_length=50, blank=False)
    titulo = models.CharField(max_length=240,blank=False)
    descricao = models.CharField(max_length=500, blank=False)
    capa = models.URLField(max_length=1024, null=True, blank=True)
    data_atual = models.DateField(auto_now=True)
    link_noticia = models.URLField(max_length=1024, null=True, blank=True)
    
    def __str__(self):
        return self.titulo
  
