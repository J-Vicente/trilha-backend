
# Sistema de E-commerce em Django

Este projeto é um sistema de e-commerce desenvolvido com Django. Permite aos usuários navegar por produtos, realizar compras e aos administradores gerenciar o estoque, produtos e ver o faturamento.

## Instalação

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clonar o repositório

```bash
git clone --branch django --single-branch https://github.com/J-Vicente/trilha-backend.git
cd NOME_DO_REPOSITORIO
```

### 2. Criar e ativar um ambiente virtual

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Aplicar as migrações

```bash
python manage.py migrate
```

### 5. Rodar o servidor

```bash
python manage.py runserver
```

Acesse o site em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Login como administrador

Para acessar como administrador(editar/excluir produtos, ver faturamento):

Login:
Usuário: Administrador
Senha: senha123

Na área de gerenciamento é possível cadastrar novos admnistradores.

---

## Tecnologias e frameworks utilizados

- **Python**
- **Django** – backend e sistema de autenticação
- **SQLite** – banco de dados padrão (pode ser alterado para PostgreSQL, MySQL, etc.)
- **Bootstrap** – estilização dos templates
- **Pillow** – tratamento de imagens (upload de fotos de produtos)
- **HTML5 / CSS3** – templates e estrutura da interface
