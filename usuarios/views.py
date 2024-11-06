from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib import auth
from empresarios.models import Empresas


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar')
    
    return redirect('/usuarios/redirecionamento')

def cadastro(request):
    if(request.method == "GET"):
        
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if(senha != confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas devem ser iguais')
            return redirect('/usuarios/cadastro')
        
        if(len(senha) <6):
            messages.add_message(request, constants.ERROR, 'A senha deve possuir ao menos 6 caracteres')
            return redirect('/usuarios/cadastro')
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existente')
            return redirect('/usuarios/cadastro')
        
        usuario = User.objects.create_user(
            username= username,
            password = senha

        )   
        return redirect('/usuarios/logar')
        

def logar(request):
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            
            return redirect('/empresarios/cadastrar_empresa')

        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
        return redirect('/usuarios/logar')


def redirecionamento(request):

    user_id = request.user.id

    if request.method == 'GET':
        return render(request, 'redirecionamento.html', {'user_id':user_id})
    

    
