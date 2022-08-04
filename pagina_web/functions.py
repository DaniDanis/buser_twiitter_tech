from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from .models import *
from .functions import *
import json
import requests

# funcao que importa dados da API DE NOTICIA
def sidebar(url):
    # article = {}   
    if Noticias.objects.all().count() < 60:
        try:
            article = get_noticias(url)
        except:
            article = Noticias.objects.all().order_by('-data_atual')
    else:
        Noticias.objects.filter(data_atual = (datetime.today() - timedelta(days=1))).delete() #deleta os posts com a data de ontem
        article = get_noticias(url) #recebe novos posts
    return article  

def get_noticias(url):
    headers = {"Ocp-Apim-Subscription-Key" : '19a984ff47ec4a20acd1cf0657be1e42'}
    params  = {"mkt": "pt-BR", "q": "", "textDecorations": True, "textFormat": "HTML", "count": 10}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    data = json.loads(search_results)
    articles = data['value']


    for ar in articles:
        try:
            dados_noticias = Noticias(
                autor= ar['provider'][0]['name'],
                titulo = ar['name'],
                descricao= ar['description'],
                capa= ar['image']['thumbnail']['contentUrl'],
                link_noticia = ar['url'],
            )
            dados_noticias.save()
        except (KeyError, ConnectionRefusedError, ValueError) as error:
            pass
    article = Noticias.objects.all().order_by('-data_atual')
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
    post_id = request.POST.get('post_id')
    post = Posts.objects.get(id = post_id)
    if PostLike.objects.filter(user = request.user, post = post):
        PostLike.objects.get(post=post, user=request.user).delete()
    else:
        PostLike.objects.create(user=request.user, post=post).save()
        
        
      #faz zip de like vs numero de likes  
def contador_de_like(*banco):
    post_x_like = []
    
    for b in banco[0]:
        quant_likes = b.likes.count()
        post_x_like.append([b.id, quant_likes])
    return post_x_like


def retorna_users():
    User = get_user_model()
    users = User.objects.all()
    return users

