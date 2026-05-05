from django.shortcuts import render


# Create your views here.


def login(request):
   render(request,'usuarios_auth/login.html')

def criar_conta(request):
   render(request,'usuarios_auth/criar_conta.html')
   
def trocar_senha(request):
   render(request,'usuarios_auth/trocar_senha.html')