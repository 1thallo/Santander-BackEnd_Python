# FastAPI
### Quem é o FastAPI?
Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção.
FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

### Async
Código assíncrono apenas significa que a linguagem tem um jeito de dizer para o computador / programa que em certo ponto, ele terá que esperar por algo para finalizar em outro lugar

# Projeto
## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

# Certificado de Conclusão
<img width="1120" height="788" alt="image" src="https://github.com/user-attachments/assets/d2ab32d9-5fd6-4b32-b48c-b61a368462e6" />


## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`, `fastapi-pagination`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

## Funcionalidades Implementadas

### 🔍 Query Parameters
- **Atletas**: Filtros por `nome` e `cpf`
  ```
  GET /atletas/?nome=João&cpf=12345678901
  ```

### 📄 Paginação
- Implementada em todos os endpoints de listagem usando `fastapi-pagination`
- Parâmetros: `limit` e `offset`
  ```
  GET /atletas/?limit=10&offset=20
  GET /categorias/?limit=5&offset=0
  GET /centro-treinamento/?limit=15&offset=30
  ```

### 🎨 Response Customizado
- **Atletas**: Retorna nomes das entidades relacionadas em vez de IDs
  ```json
  {
    "items": [
      {
        "id": "uuid-here",
        "nome": "João Silva",
        "centro_treinamento": "Centro Olímpico",
        "categoria": "Scale",
        "cpf": "12345678901",
        "idade": 25,
        "peso": 75.5,
        "altura": 1.70,
        "sexo": "M"
      }
    ],
    "total": 1,
    "page": 1,
    "size": 50
  }
  ```

### ⚠️ Tratamento de Exceções de Integridade
- Captura `sqlalchemy.exc.IntegrityError` em todos os módulos
- Status code: `303` (See Other)
- Mensagens específicas por entidade:
  - **Atletas**: "Já existe um atleta cadastrado com o cpf: x"
  - **Categorias**: "Já existe uma categoria cadastrada com o nome: x"
  - **Centro de Treinamento**: "Já existe um centro de treinamento cadastrado com o nome: x"

## Execução da API

Para executar o projeto, utilizei a [pyenv](https://github.com/pyenv/pyenv), com a versão 3.11.4 do `python` para o ambiente virtual.

Caso opte por usar pyenv, após instalar, execute:

```bash
pyenv virtualenv 3.11.4 workoutapi
pyenv activate workoutapi
pip install -r requirements.txt
```

**Alternativamente, usando venv:**

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\Activate.ps1
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
```

Para subir o banco de dados, caso não tenha o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
make run-docker
```

**Ou diretamente:**
```bash
docker-compose up -d
```

Para criar uma migration nova, execute:

```bash
make create-migrations d="nome_da_migration"
```

**Ou diretamente:**
```bash
alembic revision --autogenerate -m "nome_da_migration"
```

Para criar o banco de dados, execute:

```bash
make run-migrations
```

**Ou diretamente:**
```bash
alembic upgrade head
```

## API

Para subir a API, execute:
```bash
make run
```

**Ou diretamente:**
```bash
uvicorn workout_api.main:app --reload
```

e acesse: http://127.0.0.1:8000/docs

## Endpoints Disponíveis

### 🏃‍♂️ Atletas
- `POST /atletas/` - Criar atleta
- `GET /atletas/` - Listar atletas (com filtros: nome, cpf e paginação)
- `GET /atletas/{id}` - Buscar atleta por ID

### 🏆 Categorias  
- `POST /categorias/` - Criar categoria
- `GET /categorias/` - Listar categorias (com paginação)
- `GET /categorias/{id}` - Buscar categoria por ID

### 🏢 Centro de Treinamento
- `POST /centro-treinamento/` - Criar centro de treinamento
- `GET /centro-treinamento/` - Listar centros (com paginação)
- `GET /centro-treinamento/{id}` - Buscar centro por ID

## Exemplos de Uso

### Criando um Atleta
```bash
curl -X POST "http://127.0.0.1:8000/atletas/" \
-H "Content-Type: application/json" \
-d '{
  "nome": "João Silva",
  "cpf": "12345678901",
  "idade": 25,
  "peso": 75.5,
  "altura": 1.70,
  "sexo": "M",
  "categoria_id": "uuid-da-categoria",
  "centro_treinamento_id": "uuid-do-centro"
}'
```

### Buscando Atletas com Filtros
```bash
# Por nome
curl "http://127.0.0.1:8000/atletas/?nome=João"

# Por CPF
curl "http://127.0.0.1:8000/atletas/?cpf=12345678901"

# Com paginação
curl "http://127.0.0.1:8000/atletas/?limit=10&offset=0"

# Combinando filtros e paginação
curl "http://127.0.0.1:8000/atletas/?nome=João&limit=5&offset=10"
```

## Estrutura do Projeto

```
workout_api/
├── workout_api/
│   ├── atleta/
│   │   ├── controller.py    # Endpoints + query params + paginação
│   │   ├── models.py        # Modelo SQLAlchemy
│   │   └── schemas.py       # Schemas Pydantic (response customizado)
│   ├── categorias/
│   │   ├── controller.py    # Endpoints + tratamento de exceções
│   │   ├── models.py
│   │   └── schemas.py
│   ├── centro_treinamento/
│   │   ├── controller.py    # Endpoints + tratamento de exceções  
│   │   ├── models.py
│   │   └── schemas.py
│   ├── contrib/
│   │   ├── dependencies.py  # Dependências do FastAPI
│   │   └── models.py        # Modelo base
│   ├── configs/
│   │   ├── database.py      # Configuração do banco
│   │   └── settings.py      # Configurações da aplicação
│   └── main.py              # Aplicação principal + paginação
├── alembic/                 # Migrações do banco
├── docker-compose.yml       # Configuração do PostgreSQL
├── requirements.txt         # Dependências
└── README.md
```

# Melhorias Implementadas

## ✅ Concluídas
- [x] Query parameters nos endpoints de atletas (nome, cpf)
- [x] Response customizado para atletas (nomes em vez de IDs)
- [x] Tratamento de exceções de integridade com status 303
- [x] Paginação com fastapi-pagination (limit e offset)

## 🚀 Funcionalidades Adicionais
- Validações robustas com Pydantic
- Relacionamentos SQLAlchemy otimizados
- Documentação automática com Swagger/OpenAPI
- Configuração flexível via variáveis de ambiente
- Estrutura modular e escalável

# Referências

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/
