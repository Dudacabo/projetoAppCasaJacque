from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm, PedidoForm, ItemPedidoForm
from .models import Pedido, Produto, ItemPedido
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.utils.timezone import now
from django.shortcuts import render

def is_admin(user):
    return user.is_superuser

# HOME
@login_required
def home(request):
    # 🔹 Últimos 5 pedidos
    pedidos = Pedido.objects.all().order_by('-id')[:5]

    # 🔹 CONTADORES
    total_pedidos = Pedido.objects.count()
    pedidos_producao = Pedido.objects.filter(status='producao').count()
    pedidos_pendentes = Pedido.objects.filter(status='pendente').count()
    pedidos_entregues_qtd = Pedido.objects.filter(status='entregue').count()

    # 🔹 BASE FINANCEIRA (somente entregues)
    pedidos_entregues = Pedido.objects.filter(status='entregue')

    # 💰 TOTAL VENDIDO
    total_vendido = sum(p.total for p in pedidos_entregues)

    # 💵 TICKET MÉDIO
    ticket_medio = (
        total_vendido / pedidos_entregues_qtd
        if pedidos_entregues_qtd > 0 else 0
    )

    # 📅 HOJE
    hoje = now().date()
    vendas_hoje = sum(
        p.total for p in pedidos_entregues
        if p.data_criacao.date() == hoje
    )

    # 📆 MÊS
    mes = now().month
    vendas_mes = sum(
        p.total for p in pedidos_entregues
        if p.data_criacao.month == mes
    )

    context = {
        "pedidos": pedidos,

        # 📊 contadores
        "total_pedidos": total_pedidos,
        "pedidos_producao": pedidos_producao,
        "pedidos_pendentes": pedidos_pendentes,
        "pedidos_entregues": pedidos_entregues_qtd,

        # 💰 financeiro
        "total_vendido": total_vendido,
        "ticket_medio": ticket_medio,
        "vendas_hoje": vendas_hoje,
        "vendas_mes": vendas_mes,
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
    query = request.GET.get('q', '').strip()

    if query:
        produtos_lista = Produto.objects.filter(nome__icontains=query)
    else:
        produtos_lista = Produto.objects.all()

    paginator = Paginator(produtos_lista, 5)  # 5 por página
    page_number = request.GET.get('page')
    produtos = paginator.get_page(page_number)

    context = {
        "produtos": produtos,
        "query": query
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
@user_passes_test(is_admin)
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
    status = request.GET.get('status')
    query = request.GET.get('q')

    pedidos_lista = Pedido.objects.all()

    # filtro por status
    if status:
        pedidos_lista = pedidos_lista.filter(status=status)

    # filtro por nome
    if query:
        pedidos_lista = pedidos_lista.filter(cliente_nome__icontains=query)

    # ordenação (boa prática)
    pedidos_lista = pedidos_lista.order_by('-id')

    # paginação
    paginator = Paginator(pedidos_lista, 5)  # 5 por página
    page_number = request.GET.get('page')
    pedidos = paginator.get_page(page_number)

    context = {
        'pedidos': pedidos,
        'status': status,
        'query': query
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
@user_passes_test(is_admin)
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



    