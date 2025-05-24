FastAPI Task API
Uma API RESTful simples com autenticação JWT para gerenciar tarefas.
Instalação

Clone o repositório:
git clone <URL_DO_REPOSITORIO>
cd project

Crie um ambiente virtual e instale as dependências:
python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
pip install -r requirements.txt

Execute a aplicação:
uvicorn src.main:app --reload

Acesse a API em http://127.0.0.1:8000/docs.

Uso

Login: Use o endpoint /token com username: user1 e password: senha123 para obter um token JWT.
Endpoints protegidos: Inclua o token no cabeçalho Authorization: Bearer <token> para acessar os endpoints /tasks.

Estrutura do Projeto

src/api/: Endpoints e roteadores da API.
src/auth/: Módulo reutilizável para autenticação JWT.
src/core/: Configurações globais.
src/models/: Modelos de dados.
src/schemas/: Esquemas Pydantic.
src/database/: Banco de dados (simulado).

Notas

Substitua a SECRET_KEY em src/core/config.py por uma chave forte em produção.
Considere usar um banco de dados real (como PostgreSQL) em vez do banco simulado.
