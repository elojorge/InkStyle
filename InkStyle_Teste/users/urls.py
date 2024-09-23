from django.urls import path
from . import views  # Importa as funções ou classes de vista desta aplicação

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),   # Rota para a página inicial da aplicação
    # Exemplo de rota: path('', views.index, name='index'),
]

