# Lojinha Sabor da Casa Jacque

Uma aplicação Django completa para gerenciamento de pedidos e produtos com sistema de autenticação.

## 📋 Descrição

Este é um projeto Django desenvolvido para gerenciar uma loja virtual com funcionalidades completas de:
- Cadastro de produtos
- Gestão de pedidos
- Controle de itens por pedido
- Sistema de autenticação de usuários
- Interface responsiva com Bootstrap

## 🚀 Tecnologias

- **Django 6.0.2** - Framework web
- **SQLite** - Banco de dados
- **Python** - Linguagem principal
- **Bootstrap 5** - Framework CSS para interface responsiva
- **Django Auth** - Sistema de autenticação nativo

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
├── pedidos/                 # App de gestão de pedidos
│   ├── migrations/         # Migrações do banco de dados
│   ├── templates/          # Templates HTML do app
│   └── views.py            # Views com autenticação
├── templates/               # Templates globais
│   ├── base.html           # Template base com navbar
│   └── registration/       # Templates de autenticação
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
- **CRUD** completo para pedidos
- **Gestão** de múltiplos itens por pedido
- **Cálculo** automático do total do pedido
- **Controle** de status de entrega

### Interface e Usabilidade
- **Design responsivo** com Bootstrap 5
- **Navbar** com informações do usuário logado
- **Botão** de logout acessível
- **Templates** customizados e modernos
- **Interface** administrativa Django

## 🌐 Acesso

- **Aplicação**: http://127.0.0.1:8000/
- **Login**: http://127.0.0.1:8000/login/
- **Admin**: http://127.0.0.1:8000/admin/

## 🔄 Fluxo de Trabalho

1. **Acesso inicial**: O usuário é redirecionado para a página de login
2. **Autenticação**: Após login válido, o usuário acessa a página inicial
3. **Navegação**: Todas as funcionalidades são acessíveis através da navbar
4. **Sessão**: O usuário pode fazer logout a qualquer momento através do botão "Sair"

## 📝 Observações

- Todas as views (exceto login) requerem autenticação obrigatória
- O sistema redireciona automaticamente para login se o usuário não estiver autenticado
- Após logout, o usuário é redirecionado para a página de login
- O nome do usuário logado é exibido na navbar

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob licença MIT.
