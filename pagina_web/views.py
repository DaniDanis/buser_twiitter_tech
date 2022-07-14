from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pagina_web.models import Posts
from pagina_web.forms import FormPost
from django.http import HttpRequest

# Create your views here.
def login(request):
    return render(request, 'registration/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

#@login_required(login_url='/')
def home(request):
    form = FormPost()
    context = {
    'Posts': Posts.objects.all(),
    'form' : form,
    }
    return render(request, 'home/home.html', context)

def menubar(request):
    return render(request, 'home/menubar.html', {})

def sidebar(request):
    return render(request, 'home/sidebar.html', {})

def explorar(request):
    return render(request, 'home/explorar.html', {})

