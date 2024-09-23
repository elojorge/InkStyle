from django.urls import path
from . import views  # Importa as funções ou classes de vista desta aplicação

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking'), # Rota para a página inicial da aplicação
    # Exemplo de rota: path('', views.index, name='index'),
]