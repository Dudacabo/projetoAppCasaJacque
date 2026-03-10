from django.urls import path
from pedidos import views

app_name = 'pedidos'

urlpatterns = [
    #HOME
    path('', views.home, name='home'),
    #PRODUTOS
    path('produto/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produto/listar/', views.listar_produto , name='listar_produto'),
    path('produto/editar/<int:id>/', views.editar_produto , name='editar_produto'),
    path('produto/excluir/<int:id>/', views.excluir_produto , name='excluir_produto'),
    # PEDIDOS 
    path('pedido/cadastrar/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('pedido/listar/', views.listar_pedido , name='listar_pedido'),
    path('pedido/editar/<int:id>/', views.editar_pedido , name='editar_pedido'),
    path('pedido/excluir/<int:id>/', views.excluir_pedido , name='excluir_pedido'),
]
