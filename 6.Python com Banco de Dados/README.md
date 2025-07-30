# 📊 Módulo 06 - Integração Python com Banco de Dados

## 📋 Visão Geral

Este módulo aborda a integração completa entre Python e diferentes tipos de bancos de dados, explorando desde conceitos fundamentais até implementações práticas com tecnologias relacionais e NoSQL. O foco está em técnicas de modelagem, conexão segura, operações CRUD e otimização de performance.

## 🎯 Objetivos de Aprendizagem

- Compreender os fundamentos e diferenças entre bancos relacionais e NoSQL
- Dominar a Python DB API (PEP 249) para operações com SQLite
- Implementar soluções com MongoDB usando PyMongo
- Aplicar estratégias de Schema Design para documentos
- Otimizar consultas com índices e agregações
- Conhecer outros SGBDs NoSQL (Redis, Neo4J, Cassandra)

## Certificado de Conclusão de Módulo

![Certificado](https://github.com/user-attachments/assets/c18ac55c-6aae-41aa-9992-61f4581fb80e)

## 📚 Conteúdo Programático

### 1. **Introdução a Banco de Dados**

- Tipos de banco de dados (SQL vs NoSQL)
- Conceitos de tabelas e documentos
- DBMS e suas características
- Tipos de dados e modelagem

### 2. **Banco de Dados Relacionais**

- Fundamentos de SQL
- Joins e subconsultas
- Consultas avançadas
- Normalização e relacionamentos

### 3. **NoSQL e MongoDB**

- **Introdução aos Bancos NoSQL**
  - Redis (chave-valor)
  - Neo4J (grafos)
  - Cassandra (colunar)
- **MongoDB Fundamentals**
  - Setup com Docker
  - Operações CRUD
  - Consultas com operadores ($in, $or, $lt, $lte)
- **Schema Design**
  - Embedding vs Referência
  - Padrões de modelagem (1:1, 1:N, N:N)
  - Otimização de performance

### 4. **Python DB API e BD Relacional**

- Conexão com SQLite usando Python
- Operações CRUD seguras com placeholders
- Context managers para gerenciamento de recursos
- Transações e controle de concorrência

### 5. **Hands-on: Projetos Práticos**

- Sistema de clientes com SQLite
- Manipulação de dados no MongoDB
- Agregações e consultas complexas
- Implementação de índices

## 🛠️ Tecnologias Utilizadas

### **Bancos de Dados:**

- **SQLite** - Banco relacional embarcado
- **MongoDB** - Banco de documentos NoSQL
- **Redis** - Cache e estruturas de dados em memória
- **Neo4J** - Banco de grafos
- **Cassandra** - Banco orientado a colunas

### **Bibliotecas Python:**

- **sqlite3** - Interface nativa para SQLite
- **pymongo** - Driver oficial para MongoDB
- **pathlib** - Manipulação de caminhos de arquivos

### **Ferramentas de Desenvolvimento:**

- **Docker & Docker Compose** - Containerização do MongoDB
- **VS Code Extensions** - MongoDB, Docker, Redis
- **MongoDB Compass** - Interface gráfica para MongoDB

## 🔧 Principais Funcionalidades Desenvolvidas

### **Operações CRUD:**

- Inserção de dados únicos e em lote
- Consultas com filtros e ordenação
- Atualizações condicionais
- Deleção segura de registros

### **Consultas Avançadas:**

- Joins e subconsultas em SQL
- Agregations pipelines no MongoDB
- Operadores de comparação e lógicos
- Busca textual e indexação

### **Otimizações de Performance:**

- Índices simples e compostos
- Context managers para conexões
- Tratamento de erros e validações
- Connection pooling

### **Modelagem de Dados:**

- Schema design flexível no MongoDB
- Relacionamentos entre documentos
- Denormalização estratégica
- Padrões de design para escalabilidade

## 🚀 Como Executar

### **Pré-requisitos:**

```bash
# Instalar dependências Python
pip install pymongo

# Para MongoDB com Docker
docker-compose up -d
```

### **SQLite (nativo):**

```bash
python DB-API.py
```

### **MongoDB:**

```bash
# Executar playground no VS Code
# Abrir arquivo .mongodb.js
# Usar: Ctrl+Shift+P > "MongoDB: Run Selected Lines"
```

### **Outros SGBDs NoSQL:**

- **Redis:** Usar Redis CLI ou RedisInsight
- **Neo4J:** Browser web ou Neo4J Desktop
- **Cassandra:** Astra DataStax (cloud)

## 💡 Conceitos-Chave Abordados

### **Modelagem de Dados em diferentes bancos:**

- **Relacional:** Normalização, relacionamentos, integridade referencial
- **Documento:** Embedding vs Referência, flexibilidade de schema
- **Grafos:** Nós, relacionamentos, consultas baseadas em caminhos
- **Chave-Valor:** Estruturas simples, cache, sessões

### **Performance e Otimização:**

- Índices adequados para cada tipo de consulta
- Agregações eficientes
- Connection pooling e reutilização
- Monitoramento de queries

### **Segurança e Boas Práticas:**

- Prevenção de SQL/NoSQL injection
- Gerenciamento adequado de conexões
- Validação de dados de entrada
- Tratamento robusto de erros

### **Python DB API:**

- Padrão PEP 249 para uniformidade
- Context managers para recursos
- Transações e controle de concorrência
- Placeholders para segurança

## 📈 Resultados de Aprendizagem

Habilidades desenvolvidas no módulo:

- ✅ Escolher o tipo de banco adequado para cada projeto
- ✅ Implementar operações CRUD seguras em Python
- ✅ Modelar dados eficientemente para SQL e NoSQL
- ✅ Otimizar consultas e melhorar performance
- ✅ Integrar múltiplas tecnologias de banco em uma aplicação
- ✅ Aplicar boas práticas de segurança e tratamento de erros

## 🔗 Recursos Complementares

- **MongoDB University** - Cursos oficiais gratuitos
- **SQLite Documentation** - Referência completa
- **Python PEP 249** - Especificação da DB API
- **Redis Commands** - Referência de comandos
- **Neo4J Cypher** - Linguagem de consulta para grafos

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 06 - Integração Python com Banco de Dados
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa
