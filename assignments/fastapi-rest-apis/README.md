# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST simples usando o framework FastAPI em Python. Os alunos irão aprender a definir endpoints, modelos de dados (Pydantic), validar entradas, e executar a aplicação localmente com o Uvicorn.

## 📝 Tasks

### 🛠️	Build a Small REST API

#### Description
Implemente uma API que gerencia um pequeno recurso (por exemplo: tarefas/to-dos ou notas). A API deve suportar operações básicas CRUD: criar, ler (lista e por id), atualizar e deletar. Utilize Pydantic para modelos de request/response e trate erros comuns (400/404).

#### Requirements
Completed program should:

- Use FastAPI to define routes/endpoints.
- Define request and response models with Pydantic.
- Implement endpoints for: list all, get by id, create, update, delete.
- Validate incoming data and return appropriate HTTP status codes.
- Include basic in-memory storage (lista/dicionário) — não é necessário banco de dados.
- Provide automatic interactive docs via Swagger UI (FastAPI já inclui).
- Be runnable from the command line (e.g., `uvicorn starter_code:app --reload`).

#### Example endpoints (suggested)

- GET /items — lista todos os itens
- GET /items/{id} — retorna item por id
- POST /items — cria novo item
- PUT /items/{id} — atualiza item existente
- DELETE /items/{id} — remove item

#### How to run (dev)

1. Instale dependências:

```bash
pip install -r requirements.txt
```

2. Inicie o servidor:

```bash
uvicorn starter_code:app --reload
```

3. Abra a interface interativa: `http://127.0.0.1:8000/docs`

---

Siga o template do curso ao submeter: inclua seu código em `starter-code.py` dentro desta pasta da atribuição. Opcionalmente adicione testes simples em `tests/`.
