from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from .forms import form_TextoPost
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import *


# Create your views here.
def select_register(request):
    return render(request, 'home/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

@login_required(login_url='opcoes')
def home(request):
    
    # url do bing noticias
    articles = sidebar("https://api.bing.microsoft.com/v7.0/news/search")
    
    posts = Posts.objects.filter(is_comment__isnull = True)
    posts_vs_likes = contador_de_like(posts)
    n = limite_posts(posts)
    posts_curtidos = retorna_lista_de_posts_curtidos(request, banco_PostLike=PostLike)
    context = {
        'numero_de_posts' : n,
        'Posts': posts.order_by('-date')[:n],
        'form_texto_post': form_TextoPost(),
        'articles': articles, 
        'posts_curtidos' : posts_curtidos,
        'post_original': False,
        'posts_vs_likes': posts_vs_likes,
        # 'profiles': Profile.objects.get(),
           
    }
    verifica_se_eh_post_e_salva(request, banco_user=User, banco_posts=Posts)
    context['form_texto_post']: form_TextoPost()
    if request.method == 'POST':
        return redirect(reverse('home'))
    return render(request, 'home/home.html', context)
def menubar(request):
    return render(request, 'home/menubar.html', {})

def explorar(request):
    return render(request, 'home/explorar.html', {})

def login(request):
    return render(request, 'home/login.html', {})

def curtir_action(request, post_id):
   crud_postlike(request, post_id)
   return JsonResponse({})

def tocomment(request):
    texto = request.POST['text-input']
    user = request.user 
    post = Posts.objects.get(id = request.POST['input-post-id'])
    if texto:
        Posts.objects.create(user=user, texto=texto, is_comment = post).save()

    host = request.META['HTTP_REFERER']
    return redirect(host)


def postdetails(request, post_id):
    posts = Posts.objects.filter(is_comment=Posts.objects.get(id = post_id) ).order_by("-date")
    n = limite_posts(posts)
    posts_curtidos = retorna_lista_de_posts_curtidos(request, banco_PostLike=PostLike)
    
    context = {
        'numero_de_posts' : n,
        'Posts': posts.order_by('-date')[:n],
        'form_texto_post': form_TextoPost(),
        'posts_curtidos' : posts_curtidos,
        'post_original': Posts.objects.get(id = post_id),
    }
    verifica_se_eh_post_e_salva(request, banco_user=User, banco_posts=Posts)
    context['form_texto_post']: form_TextoPost()
    return render(request,'home/home.html',context)

   
