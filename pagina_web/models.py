from pickle import NONE
from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now=True)
    texto = models.CharField(max_length=240,blank=True)
    is_retweet = models.ForeignKey('self', null=True,blank=True,  on_delete=models.CASCADE, related_name="retweets")
    is_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name = 'comentarios')
    
    
class PostLike(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")


  
