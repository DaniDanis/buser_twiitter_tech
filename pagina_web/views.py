from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pagina_web.models import *
from pagina_web.forms import form_TextoPost
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import requests
from pagina_web.functions import *


# Create your views here.
def select_register(request):
    return render(request, 'home/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

@login_required(login_url='opcoes')
def home(request):
    article = sidebar("https://newsapi.org/v1/articles?country=br&source=bbc-news&sortBy=top&apiKey=f3ddd76e328349ce8967b46f7703dfad")
    
    n = limite_posts(Posts.objects.all())
    posts_curtidos = retorna_lista_de_posts_curtidos(request, banco_PostLike=PostLike)
    context = {
        'numero_de_posts' : n,
        'Posts': Posts.objects.all().order_by('-date')[:n],
        'form_texto_post': form_TextoPost(),
        'articles': article, 
        'posts_curtidos' : posts_curtidos,
           
    }
    verifica_se_eh_post_e_salva(request, banco_user=User, banco_posts=Posts)
    return render(request,'home/home.html',context)

def menubar(request):
    return render(request, 'home/menubar.html', {})

def explorar(request):
    return render(request, 'home/explorar.html', {})

def login(request):
    return render(request, 'home/login.html', {})