from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    cliente_nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('producao', 'Em Produção'),
        ('entregue', 'Entregue'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    @property
    def total(self):
        return sum(
            item.produto.preco * item.quantidade
            for item in self.itens.all()
        )
    
    def __str__(self):
        return f"Pedido {self.id} - {self.cliente_nome}"
    

class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="itens"
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE
    )
    quantidade = models.PositiveIntegerField()

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"



