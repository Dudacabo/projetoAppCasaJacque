from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm, PedidoForm, ItemPedidoForm
from .models import Pedido, Produto, ItemPedido
from django.http import HttpResponse

def home(request):
    produtos = Produto.objects.all().order_by('-id')[:5]
    pedidos = Pedido.objects.all().order_by('-id')[:5]

    context = {
         "produtos": produtos,
         'pedidos': pedidos
     }
    return render(request, "home.html", context)



def cadastrar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("pedidos:listar_produto")
        
    else:
         form = ProdutoForm()

    context = {
            "form": form
        }
    return render(request, "produtos/cadastrar_produto.html", context)


def listar_produto(request):
     produtos = Produto.objects.all()

     context = {
         "produtos": produtos
     }
     return render(request, "produtos/listar_produto.html", context)


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            return redirect("pedidos:listar_produto")
        
    else:
        form = ProdutoForm(instance=produto)
    
    context = {
        "form": form
    }

    return render(request, "produtos/editar_produto.html", context)


def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.delete()
        return redirect('pedidos:listar_produto')
    
    return render(request, 'produtos/excluir_produto.html', {'produto': produto} )


def cadastrar_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("pedidos:listar_pedido")

    else:
        form = PedidoForm()

    context = {
        'form': form
    }
    return render(request, "pedidos/cadastrar_pedido.html", context)


def listar_pedido(request):
    pedidos = Pedido.objects.all()

    context = {
        'pedidos': pedidos
    }
    return render(request, 'pedidos/listar_pedido.html', context)


def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)

        if form.is_valid():
            form.save()
            return redirect("pedidos:listar_pedido")
        
    else:
        form = PedidoForm(instance=pedido)

    context = {
        'form': form
    }
    return render(request, "pedidos/editar_pedido.html", context)


def excluir_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == "POST":
        pedido.delete()
        return redirect("pedidos:listar_pedido")
    return render(request, "pedidos/excluir_pedido.html", {'pedidos': pedido})

    