# Lojinha Django

Uma aplicação Django simples para gerenciamento de pedidos e produtos.

## 📋 Descrição

Este é um projeto Django desenvolvido para gerenciar uma loja virtual com funcionalidades básicas de:
- Cadastro de produtos
- Gestão de pedidos
- Controle de itens por pedido

## 🚀 Tecnologias

- **Django 6.0.2** - Framework web
- **SQLite** - Banco de dados
- **Python** - Linguagem principal

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Dudacabo/projetoAppCasaJacque.git
cd projetoAppCasaJacque
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## 🗂️ Estrutura do Projeto

```
Sabor_Casa/
├── lojinha/          # Configurações principais do Django
├── pedidos/          # App de gestão de pedidos
├── db.sqlite3        # Banco de dados SQLite
├── manage.py         # Script de gerenciamento Django
└── requirements.txt  # Dependências do projeto
```

## 🏗️ Models

### Produto
- `nome`: Nome do produto (max 100 chars)
- `descricao`: Descrição detalhada
- `preco`: Preço decimal (8 dígitos, 2 casas decimais)
- `ativo`: Status do produto

### Pedido
- `cliente_nome`: Nome do cliente
- `data_criacao`: Data de criação automática
- `entregue`: Status de entrega
- `total`: Calculado automaticamente

### ItemPedido
- `pedido`: Relacionamento com Pedido
- `produto`: Relacionamento com Produto
- `quantidade`: Quantidade do item

## 🔧 Funcionalidades

- **CRUD** completo para produtos
- **Gestão** de pedidos com múltiplos itens
- **Cálculo** automático do total do pedido
- **Interface** administrativa Django
- **Templates** customizados

## 🌐 Acesso

- **Aplicação**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT.
