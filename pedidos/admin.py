from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Produto, Pedido, ItemPedido


@admin.register(Produto)
class ProdutoAdmin(ImportExportModelAdmin):
    list_display = ("nome", "preco", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome",)


@admin.register(ItemPedido)
class ItemPedidoAdmin(ImportExportModelAdmin):
    list_display = ("pedido", "produto", "quantidade")


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(Pedido)
class PedidoAdmin(ImportExportModelAdmin):
    list_display = ("id", "cliente_nome", "status", "data_criacao")
    list_filter = ("status",)
    inlines = [ItemPedidoInline]