from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def pagina_inicial(request):
    return render(request, 'registration/pagina_cadastro.html', {})

def login(request):
    return render(request, 'registration/login.html', {})

def registro(request):
    if request.method =='POST':
        nome = request.POST.get('nome',None)
        sobrenome = request.POST.get('sobrenome',None)
        email = request.POST.get('email',None)
        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha',None)
        senha2 = request.POST.get('senha2',None)
        if senha == senha2:            
            user = User.objects.create_user(email = email, username= usuario, password =senha)
            user.save()
            messages.success(
                request,
                'Visitante Registrado com sucesso !!!'
            )
            return redirect('/home/')
        else:
            messages.error(
                request,
                'Erro !!!')
    return render(request, 'registration/registro.html')

@login_required
def logout(request):
    logout(request)
    return redirect('/home/')