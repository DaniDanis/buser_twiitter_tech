from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pagina_web.models import Posts
from pagina_web.forms import form_TextoPost
from django.http import HttpRequest
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'registration/pagina_cadastro.html', {})

def base(request):
    return render(request, 'home/base.html', {})

# RONALD~ mexido para pegar os dados do post
#@login_required(login_url='/')
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
    return render(request, 'home/sidebar.html', {})

def explorar(request):
    return render(request, 'home/explorar.html', {})

