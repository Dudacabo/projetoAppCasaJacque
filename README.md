# APP GERENCIADOR DE PEDIDOS E PRODUTOS PARA LOJA

Uma aplicação Django completa para gerenciamento de pedidos e produtos com sistema de autenticação.

## 📋 Descrição

Este é um projeto Django completo desenvolvido para gerenciar uma loja virtual com funcionalidades robustas de:
- **Cadastro e gestão** de produtos com controle de ativação
- **Sistema completo** de pedidos com múltiplos status
- **Controle detalhado** de itens por pedido
- **Sistema de autenticação** obrigatório para todas as funcionalidades
- **Interface responsiva** e moderna com Bootstrap 5
- **Painel administrativo** Django integrado

## 🚀 Tecnologias

- **Django 6.0.2** - Framework web principal
- **Python 3.x** - Linguagem de programação
- **Bootstrap 5** - Framework CSS para design responsivo
- **Django Auth** - Sistema de autenticação nativo
- **Django Templates** - Sistema de templates HTML
- **Django Forms** - Validação e processamento de formulários

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

5. Crie um superusuário para acessar o sistema:
```bash
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## 🗂️ Estrutura do Projeto

```
Sabor_Casa/
├── lojinha/                 # Configurações principais do Django
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py            # URLs principais (login, logout)
│   └── wsgi.py            # Servidor WSGI
├── pedidos/                 # App principal de gestão
│   ├── migrations/         # Migrações do banco de dados
│   ├── templates/          # Templates HTML organizados
│   │   ├── produtos/       # Templates de produtos
│   │   ├── pedidos/       # Templates de pedidos
│   │   ├── item_pedido/    # Templates de itens
│   │   └── registration/   # Templates de autenticação
│   ├── admin.py           # Configuração admin Django
│   ├── forms.py           # Formulários personalizados
│   ├── models.py          # Models do banco de dados
│   ├── urls.py            # URLs do app pedidos
│   └── views.py           # Views com autenticação
├── templates/               # Templates globais
│   └── base.html           # Template base com navbar
├── db.sqlite3              # Banco de dados SQLite
├── manage.py               # Script de gerenciamento Django
└── requirements.txt        # Dependências do projeto
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
- `status`: Status do pedido (Pendente, Em Produção, Entregue)
- `total`: Calculado automaticamente

### ItemPedido
- `pedido`: Relacionamento com Pedido
- `produto`: Relacionamento com Produto
- `quantidade`: Quantidade do item

## 🔧 Funcionalidades

### Autenticação e Segurança
- **Sistema de login** obrigatório para todas as funcionalidades
- **Logout** seguro com redirecionamento
- **Proteção** de views com decorator `@login_required`
- **Interface** personalizada de login

### Gestão de Produtos
- **CRUD** completo para produtos (Criar, Ler, Atualizar, Deletar)
- **Validação** de formulários
- **Status** de ativação/desativação de produtos

### Gestão de Pedidos
- **CRUD** completo para pedidos com validação
- **Sistema de status** com três estados: Pendente, Em Produção, Entregue
- **Gestão** de múltiplos itens por pedido
- **Cálculo** automático do total do pedido
- **Controle** granular do fluxo de trabalho

### Interface e Usabilidade
- **Design responsivo** com Bootstrap 5
- **Navbar** dinâmica com nome do usuário logado
- **Sistema de logout** seguro com redirecionamento
- **Templates** customizados e organizados por funcionalidade
- **Interface** administrativa Django completa
- **Página de login** centralizada e moderna

## 🌐 Acesso

- **Aplicação**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 🔄 Fluxo de Trabalho

1. **Acesso inicial**: Usuário é redirecionado automaticamente para `/login/`
2. **Autenticação**: Login válido redireciona para página inicial (`/`)
3. **Dashboard**: Página home mostra resumo de produtos e pedidos recentes
4. **Navegação**: Menu principal com acesso a todas as funcionalidades
5. **Gestão**: CRUD completo para produtos e pedidos
6. **Sessão**: Logout seguro com redirecionamento para página de login

## 📝 Observações

- **Segurança**: Todas as views (exceto login) exigem autenticação com `@login_required`
- **Redirecionamento automático**: Usuários não autenticados são enviados para `/login/`
- **Sessão segura**: Logout redireciona para página de login
- **Interface personalizada**: Nome do usuário exibido na navbar
- **Status de pedidos**: Sistema com três estados (Pendente, Em Produção, Entregue)
- **Cálculos automáticos**: Total dos pedidos calculado dinamicamente
- **Validação**: Formulários com validação robusta e mensagens de erro

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT.
