from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm, PedidoForm, ItemPedidoForm
from .models import Pedido, Produto, ItemPedido
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# HOME
@login_required
def home(request):
    produtos = Produto.objects.all().order_by('-id')[:5]
    pedidos = Pedido.objects.all().order_by('-id')[:5]

    context = {
         "produtos": produtos,
         'pedidos': pedidos
     }
    return render(request, "home.html", context)



# PRODUTOS
@login_required
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


@login_required
def listar_produto(request):
     produtos = Produto.objects.all().order_by('-id')

     context = {
         "produtos": produtos
     }
     return render(request, "produtos/listar_produto.html", context)


@login_required
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


@login_required
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.delete()
        return redirect('pedidos:listar_produto')
    
    return render(request, 'produtos/excluir_produto.html', {'produto': produto} )


# PEDIDOS
@login_required
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


@login_required
def listar_pedido(request):
    pedidos = Pedido.objects.all().order_by('-id')

    context = {
        'pedidos': pedidos
    }
    return render(request, 'pedidos/listar_pedido.html', context)


@login_required
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


@login_required
def excluir_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)

    if request.method == "POST":
        pedido.delete()
        return redirect("pedidos:listar_pedido")
    return render(request, "pedidos/excluir_pedido.html", {'pedido': pedido})

@login_required
def detalhar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    
    context = {
        'pedido': pedido
    }
    return render(request, "pedidos/detalhar_pedido.html", context)

# ITENS DO PEDIDO
@login_required
def adicionar_item(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == "POST":
        form = ItemPedidoForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.pedido = pedido
            item.save()
            return redirect("pedidos:detalhar_pedido", pedido.id)
    
    else:
        form = ItemPedidoForm()
    
    context = {
        'form': form,
        'pedido': pedido
    }
    return render(request, "item_pedido/adicionar_item.html", context)


@login_required
def excluir_item(request, item_id):
    item = get_object_or_404(ItemPedido, id=item_id)
    
    if request.method == "POST":
        item.delete()
        return redirect("pedidos:detalhar_pedido", item.pedido.id)
    
    return render(request, "item_pedido/excluir_item.html", {'item': item})


@login_required
def editar_item(request, item_id):
    item = get_object_or_404(ItemPedido, id=item_id)
    
    if request.method == "POST":
        form = ItemPedidoForm(request.POST, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect("pedidos:detalhar_pedido", item.pedido.id)
    
    else:
        form = ItemPedidoForm(instance=item)
    
    context = {
        'form': form,
        'item': item
    }
    return render(request, "item_pedido/editar_item.html", context)

@login_required
def listar_item(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    
    context = {
        'pedido': pedido
    }
    return render(request, "item_pedido/listar_item.html", context)



    