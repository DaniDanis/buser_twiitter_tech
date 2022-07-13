import email
from pickle import NONE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class user(models.Model):
#     user = models.CharField(max_length=17, unique=True,null=False, blank=False)
#     nome = models.CharField(max_length=18, null=False, blank=False)
#     email = models.EmailField(unique=True, max_length=64)    

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.NOT_PROVIDED)
    data = models.DateTimeField()
    texto = models.CharField(max_length=200,blank=True)

  
  
