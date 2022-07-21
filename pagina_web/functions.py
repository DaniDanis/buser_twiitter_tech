from multiprocessing import context
import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pagina_web.models import *
from pagina_web.forms import form_TextoPost
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pagina_web.functions import *
import json
import requests

# funcao que importa dados da API DE NOTICIA
def sidebar(url):
    # url = requests.get(url)
    
    # text = url.text
    # data = json.loads(text)
    # if data['status'] != 'error':
    #     article = data['articles']
    # else:
    #     article = "............................................................................."  
    
    # return article
    
    
    headers = {"Ocp-Apim-Subscription-Key" : '19a984ff47ec4a20acd1cf0657be1e42'}
    params  = {"mkt": "pt-BR", "q": "", "textDecorations": True, "textFormat": "HTML", "count": 100, "cc": "BR"}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    data = json.loads(search_results)
    article = data['value']
    return article  

# retorna o NÚMERO de ~POSTS que pode ter na página
def limite_posts(lista_de_objetos_post):
    if len(lista_de_objetos_post) >= 17:
        n = 17
    else:
        n = len(lista_de_objetos_post)
    return n+1

# verifica se é um ~POST e se for salva no ~BANCO DE DADOS
def verifica_se_eh_post_e_salva(request, banco_user, banco_posts):
    if request.method == 'POST':
        user= banco_user.objects.get(id = request.user.id)
        banco_posts.objects.create(user=user,texto = request.POST['text-input'] ).save()
        
# Retorna lista do id todos os POSTS curtidos pelo usuário
def retorna_lista_de_posts_curtidos(request, banco_PostLike, ):
   lista_de_posts = [] 
   for i in banco_PostLike.objects.filter(user_id = request.user.id):
        lista_de_posts.append(i.post)
   return  lista_de_posts

