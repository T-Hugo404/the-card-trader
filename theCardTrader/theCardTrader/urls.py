"""
URL configuration for theCardTrader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#rotas de apps

from home import views as views_principais
from cards import views as cards
from usuarios_auth import views as auth
from usuarios_info import views as user_infos

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #rotas da home
    path('', views_principais.principal, name = 'home'),
    
    #rotas de cards
    path('cartas/',cards.cartas, name='lista_de_cartas'),
    path('detalhamento/carta/',cards.cartas_detalhamento,name='detalhes_da_carta'),
    path('detalhamento/deck/',cards.decks_detalhamento,name='detalhes_do_deck'),
    
    #rotas para autenticação
    
    path('login/',auth.login, name='login'),
    path('cadastro/',auth.criar_conta, name='cadastro'),
    path('mudarsenha/',auth.trocar_senha, name='mudar_senha'),
    
    
    
    #rotas para informações do usuário
    
    path('usuario/',user_infos.dados_usuario, name='dados_usuario'),
    path('usuario/historico/',user_infos.historico_usuario, name='historico_usuario'),
    
    
    
]
