from django.contrib import admin
from .models import Produto, Pedido, ItemPedido


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome",)


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade")


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente_nome", "status", "data_criacao")
    list_filter = ("status",)
    inlines = [ItemPedidoInline]