from datetime import datetime, timedelta
import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import form_TextoPost
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .functions import *
import json
import requests

# funcao que importa dados da API DE NOTICIA

def get_noticias(url):
    headers = {"Ocp-Apim-Subscription-Key" : '19a984ff47ec4a20acd1cf0657be1e42'}
    params  = {"mkt": "pt-BR", "q": "", "textDecorations": True, "textFormat": "HTML", "count": 10}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    data = json.loads(search_results)
    articles = data['value']
    article={}

    for ar in articles:
        dados_noticias = Noticias(
            autor= ar['provider'][0]['name'],
            titulo = ar['name'],
            descricao= ar['description'],
            capa= ar['image']['thumbnail']['contentUrl'],
            link_noticia = ar['ampUrl'],
        )
        
        dados_noticias.save()
        article = Noticias.objects.all().order_by('-data_atual')
        return article

def sidebar(url):  
    
    if Noticias.objects.all().count() < 60:
        try:
            article = get_noticias(url)
            
        except:
            article = Noticias.objects.all().order_by('-data_atual')
    else:
        Noticias.objects.get(data_atual = (datetime.today() - timedelta(days=1))).delete() #deleta os posts com a data de ontem
        article = get_noticias(url) #recebe novos posts
    return article  

# retorna o NÚMERO de ~POSTS que pode ter na página
def limite_posts(lista_de_objetos_post):
    if len(lista_de_objetos_post) >= 17:
        n = 17
    else:
        n = len(lista_de_objetos_post)
    return n

# verifica se é um ~POST e se for salva no ~BANCO DE DADOS
def verifica_se_eh_post_e_salva(request, banco_user, banco_posts):
    if request.method == 'POST':
        if request.POST['text-input']:
            user= banco_user.objects.get(id = request.user.id)
            banco_posts.objects.create(user=user,texto = request.POST['text-input'] ).save()
        
# Retorna lista do id todos os POSTS curtidos pelo usuário
def retorna_lista_de_posts_curtidos(request, banco_PostLike, ):
   lista_de_posts = [] 
   for i in banco_PostLike.objects.filter(user_id = request.user.id):
        lista_de_posts.append(i.post)
   return  lista_de_posts

# Insere POST no POSTLIKE BANCO DE DADOS
def crud_postlike(request):
    post_id = json.loads(request.body)['post_id']
    post = Posts.objects.get(id = post_id)
    if PostLike.objects.filter(user = request.user, post = post):
        PostLike.objects.get(post=post, user=request.user).delete()
    else:
        PostLike.objects.create(user=request.user, post=post).save()
