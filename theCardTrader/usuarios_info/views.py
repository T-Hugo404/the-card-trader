from django.shortcuts import render

# Create your views here.


def dados_usuario(request):
    render(request, 'usuarios_info/dados_usuario.html')
    

def historico_usuario(request):
    render(request, 'usuarios_info/historico_usuario.html')