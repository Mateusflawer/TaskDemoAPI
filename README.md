# FastAPI Task API

Uma API RESTful simples com autenticação JWT para gerenciar tarefas.

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd project
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Execute a aplicação:

   ```bash
   uvicorn src.main:app --reload
   ```

4. Acesse a API em `http://127.0.0.1:8000/docs`.

## Uso

- **Login**: Use o endpoint `/token` com `username: user1` e `password: senha123` para obter um token JWT.
- **Endpoints protegidos**: Inclua o token no cabeçalho `Authorization: Bearer <token>` para acessar os endpoints `/tasks`.

## Estrutura do Projeto

- `src/api/`: Endpoints e roteadores da API.
- `src/auth/`: Módulo reutilizável para autenticação JWT.
- `src/core/`: Configurações globais.
- `src/models/`: Modelos de dados.
- `src/schemas/`: Esquemas Pydantic.
- `src/database/`: Banco de dados (simulado).

=======
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd project
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   uvicorn src.main:app --reload
   ```

4. Acesse a API em `http://127.0.0.1:8000/docs`.

## Uso

- **Login**: Use o endpoint `/token` com `username: user1` e `password: senha123` para obter um token JWT.
- **Endpoints protegidos**: Inclua o token no cabeçalho `Authorization: Bearer <token>` para acessar os endpoints `/tasks`.

## Estrutura do Projeto

- `src/api/`: Endpoints e roteadores da API.
- `src/auth/`: Módulo reutilizável para autenticação JWT.
- `src/core/`: Configurações globais.
- `src/models/`: Modelos de dados.
- `src/schemas/`: Esquemas Pydantic.
- `src/database/`: Banco de dados (simulado).

>>>>>>> d9a70fb3f9eb2f8c8c15e615babc0ec84ff16004
## Notas

- Substitua a `SECRET_KEY` em `src/core/config.py` por uma chave forte em produção.
- Considere usar um banco de dados real (como PostgreSQL) em vez do banco simulado.
