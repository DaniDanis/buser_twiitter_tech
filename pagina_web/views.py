from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pagina_web.models import Posts
from pagina_web.forms import form_TextoPost
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
import requests


# Create your views here.
def select_register(request):
    return render(request, 'home/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

@login_required(login_url='opcoes')

# RONALD~ mexido para pegar os dados do post
def home(request):
    context = {
        'Posts': Posts.objects.all().order_by('-date'),
        'form_texto_post': form_TextoPost(), 
           
    }
    if request.method == 'POST':
        user= User.objects.get(id = request.user.id)
        Posts.objects.create(user=user,texto = request.POST['texto'] ).save()
    return render(request,'home/home.html',context)
def menubar(request):
    return render(request, 'home/menubar.html', {})

def sidebar(request):
    url = requests.get("https://newsapi.org/v1/articles?country=br&source=bbc-news&sortBy=top&apiKey=f3ddd76e328349ce8967b46f7703dfad")
    
    text = url.text
    data = json.loads(text)
    article = data['articles']
       
    return render(request, 'home/sidebar.html', context = {"articles" : article})

def explorar(request):
    return render(request, 'home/explorar.html', {})

def login(request):
    return render(request, 'home/login.html', {})