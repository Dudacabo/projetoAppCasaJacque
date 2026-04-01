from django import forms
from .models import Pedido, Produto, ItemPedido

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ("nome", "descricao", "preco", "ativo")

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite aqui'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite aqui'}),
            'preco': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control', 'placeholder': 'Digite aqui'}) ,
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'nome': "Nome do produto",
            'descricao': 'Descrição',
            'preco': 'Preço',
            'ativo': 'Ativo'
        }



class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ("cliente_nome", 'status')

        widgets = {
            'cliente_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite aqui'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'cliente_nome': "Nome do cliente",
            'status': "Status do pedido",
        }


class ItemPedidoForm(forms.ModelForm):

    class Meta:
        model = ItemPedido
        fields = ("produto", "quantidade")

        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control select-produto'}),
            'quantidade': forms.NumberInput(attrs={'min': '1', 'class': 'form-control', 'placeholder': 'Digite a quantidade aqui'}) ,
        }

        labels = {
            'produto': 'Produto',
            'quantidade': 'Quantidade',
        }

    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        if quantidade <= 0:
            raise forms.ValidationError("Quantidade deve ser maior que zero.")
        return quantidade