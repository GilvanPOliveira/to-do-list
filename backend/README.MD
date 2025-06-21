# Projeto To-Do List com FastAPI

## Descrição
Este projeto é uma API RESTful para gerenciamento de tarefas (to-do list) desenvolvida com FastAPI, SQLAlchemy e Pydantic. Ele inclui autenticação JWT para proteger as rotas e permite que usuários criem, listem, atualizem e deletem suas tarefas.

## Tecnologias Utilizadas
- Python 3.13
- FastAPI
- SQLAlchemy
- Pydantic
- JWT (JSON Web Tokens)
- SQLite (banco de dados)
- Pytest (testes automatizados)

## Estrutura do Projeto

  backend/
  │
  ├── app/
  │ ├── init.py
  │ ├── auth.py # Lógica de autenticação e JWT
  │ ├── crud.py # Operações de banco de dados para tarefas
  │ ├── database.py # Configuração do banco de dados e sessão
  │ ├── main.py # Arquivo principal da aplicação FastAPI
  │ ├── models.py # Modelos SQLAlchemy
  │ ├── schemas.py # Schemas Pydantic para validação e serialização
  │ └── routes/
  │ ├── init.py
  │ ├── auth_routes.py # Rotas de autenticação (registro, login)
  │ └── task_routes.py # Rotas para gerenciamento de tarefas
  │
  └── testes/
  ├── init.py
  ├── test_auth.py # Testes para autenticação
  └── test_tasks.py # Testes para rotas de tarefas


## Instalação
1. Clone o repositório:
  ```bash
  git clone <url-do-repositorio>
  cd backend
  ```
2. Crie e ative um ambiente virtual:
  ```bash
  python -m venv venv
  source venv/bin/activate # Linux/macOS
  venv\Scripts\activate # Windows
  ```
3. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

## Uso
1. Configure as variáveis de ambiente necessárias, como `SECRET_KEY` para JWT.
2. Execute a aplicação:
  ```bash
  uvicorn app.main:app --reload
  ```
3. A API estará disponível em `http://localhost:8000`.

## Endpoints Principais
- `POST /register`: Registrar novo usuário.
- `POST /login`: Autenticar usuário e obter token JWT.
- `GET /tarefas/`: Listar tarefas do usuário autenticado.
- `POST /tarefas/`: Criar nova tarefa.
- `PUT /tarefas/{id}`: Atualizar tarefa existente.
- `DELETE /tarefas/{id}`: Deletar tarefa.

## Autenticação
- Utiliza JWT para autenticação.
- Token deve ser enviado no header `Authorization: Bearer <token>` para acessar rotas protegidas.

## Testes
- Testes automatizados com Pytest.
- Cobrem criação de usuários, usuários duplicados, login, criação/listagem/atualização/deleção de tarefas, validação de campos e autenticação.
- Para rodar os testes:
  ```bash
  pytest -v
  ```

## Observações
- Banco de dados SQLite usado para desenvolvimento.
- Para produção, recomenda-se usar banco mais robusto e gerenciar migrações com Alembic.

## Contato
- Para dúvidas ou contribuições, abra uma issue ou envie um pull request.
- Ou entre em contato via e-mail: gilvanoliveira06@gmail.com
