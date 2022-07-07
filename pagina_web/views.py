from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'home/pagina_login.html', {})

def base(request):
    return render(request, 'home/base.html', {})