from audioop import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import form_TextoPost
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from contas.models import Profile
from django.views.static import serve
import json
import requests
from .functions import *
from django.urls.base import reverse
from django.db.models import Q


# Create your views here.
def select_register(request):
    return render(request, 'home/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

@login_required(login_url='opcoes')
def home(request):
    
    # url do bing noticias
    # article = sidebar("https://api.bing.microsoft.com/v7.0/news/search")
    article = {}
    posts = Posts.objects.filter(is_comment__isnull = True)
    n = limite_posts(posts)
    posts_curtidos = retorna_lista_de_posts_curtidos(request, banco_PostLike=PostLike)
    context = {
        'numero_de_posts' : n,
        'Posts': posts.order_by('-date')[:n],
        'form_texto_post': form_TextoPost(),
        'articles': article, 
        'posts_curtidos' : posts_curtidos,
        'post_original': False,
        # 'profiles': Profile.objects.get(),
           
    }
    verifica_se_eh_post_e_salva(request, banco_user=User, banco_posts=Posts)
    context['form_texto_post']: form_TextoPost()
    return render(request,'home/home.html',context)
def menubar(request):
    return render(request, 'home/menubar.html', {})

def explorar(request):
    return render(request, 'home/explorar.html', {})

def login(request):
    return render(request, 'home/login.html', {})

def curtir_action(request):
   crud_postlike(request)
   return JsonResponse({})

def tocomment(request):
    texto = request.POST['text-input']
    user = request.user 
    post = Posts.objects.get(id = request.POST['id_post'])
    Posts.objects.create(user=user, texto=texto, is_comment = post).save()
    return redirect(reverse("home"))


def postdetails(request, post_id):
    # url do bing noticias
    article = sidebar("https://api.bing.microsoft.com/v7.0/news/search")
    posts = Posts.objects.filter(is_comment=Posts.objects.get(id = post_id) ).order_by("-date")
    n = limite_posts(posts)
    posts_curtidos = retorna_lista_de_posts_curtidos(request, banco_PostLike=PostLike)
    
    context = {
        'numero_de_posts' : n,
        'Posts': posts.order_by('-date')[:n],
        'form_texto_post': form_TextoPost(),
        'articles': article, 
        'posts_curtidos' : posts_curtidos,
        'post_original': Posts.objects.get(id = post_id)  
    }
    verifica_se_eh_post_e_salva(request, banco_user=User, banco_posts=Posts)
    context['form_texto_post']: form_TextoPost()
    return render(request,'home/home.html',context)

   
