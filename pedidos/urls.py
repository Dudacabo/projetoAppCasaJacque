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
    path('pedido/detalhar/<int:id>/', views.detalhar_pedido , name='detalhar_pedido'),
    # ITENS DO PEDIDO
    path('pedido/adicionar-item/<int:pedido_id>/', views.adicionar_item , name='adicionar_item'),
    path('pedido/excluir-item/<int:item_id>/', views.excluir_item , name='excluir_item'),
    path('pedido/editar-item/<int:item_id>/', views.editar_item , name='editar_item'),
    path('item/listar/<int:id>/', views.listar_item , name='listar_item'),
]
