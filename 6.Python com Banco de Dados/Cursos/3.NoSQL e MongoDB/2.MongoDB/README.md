# MongoDB - Introdução e Setup

## Características
- Código aberto
- Alta performance  
- Schema-free
- JSON para armazenamento
- Suporte a índices
- Auto-sharding (Escalabilidade horizontal)
- Map Reduce para agregação
- GridFS para arquivos

## Estrutura vs SQL
| MongoDB | SQL |
|---------|-----|
| Document | Tupla/Registro |
| Collection | Tabela |
| Embedding/Linking | Join |

## Setup para Estudos

### Opção 1: MongoDB Atlas (Recomendado)

```bash
# Gratuito, sem instalação
# URL: https://www.mongodb.com/cloud/atlas
```

### Opção 2: Instalação Local

```bash
# Download: https://www.mongodb.com/try/download/community
# Incluí MongoDB Compass (GUI)
```

### Opção 3: Docker (Se WSL disponível)

```bash
docker run --name mongodb-estudo -p 27017:27017 -d mongo:latest
```

## Casos de Uso

### ✅ Quando Usar

- Grande volume de dados
- Dados semi-estruturados/não-estruturados
- Desenvolvimento ágil (schema flexível)
- Escalabilidade horizontal necessária

### ❌ Quando NÃO Usar  

- Transações ACID complexas obrigatórias
- Relacionamentos complexos frequentes
- Dados altamente estruturados e estáveis
- Compliance rígido com SQL

## Comandos Básicos

```javascript
// Ver databases
show dbs

// Usar database
use fenda_biquini

// Inserir documento
db.personagens.insertOne({
  nome: "Bob Esponja",
  profissao: "Cozinheiro",
  idade: 25
})

// Buscar documentos
db.personagens.find()
db.personagens.find({profissao: "Cozinheiro"})
```
