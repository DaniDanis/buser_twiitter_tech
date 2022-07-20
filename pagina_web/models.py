from pickle import NONE
from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.NOT_PROVIDED)
    date = models.DateTimeField(auto_now=True)
    texto = models.CharField(max_length=240,blank=True)
    is_retweet = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    
    
class PostLike(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PostComment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=240)
  
