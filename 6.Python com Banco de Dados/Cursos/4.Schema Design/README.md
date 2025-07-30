# Schema Design no MongoDB

## 🎯 Introdução

O MongoDB é **schema-free**, mas isso **NÃO** significa que você não deve pensar no design dos seus dados. Uma boa modelagem é crucial para performance, escalabilidade e manutenibilidade.

### Diferenças Fundamentais SQL vs NoSQL

| Aspecto | SQL (Relacional) | MongoDB (Documento) |
|---------|------------------|---------------------|
| **Schema** | Rígido, definido previamente | Flexível, evolui com a aplicação |
| **Relacionamentos** | Foreign Keys + JOINs | Embedding + References |
| **Normalização** | Sempre normalizado | Pode ser denormalizado |
| **Escalabilidade** | Vertical (mais CPU/RAM) | Horizontal (mais servidores) |

---

## 🔗 Embedding vs Referência

### 📦 **Embedding (Documentos Aninhados)**

Armazenar dados relacionados **dentro** do mesmo documento.

#### ✅ **Quando Usar Embedding:**

- Relação **1:1** ou **1:poucos**
- Dados sempre acessados **juntos**
- Dados filhos **não** são consultados independentemente
- **Performance** de leitura é prioridade
- Dados filhos têm **ciclo de vida** dependente do pai

#### **Exemplo Prático - E-commerce:**

```javascript
// ✅ BOM - Embedding para endereços
{
  _id: ObjectId("..."),
  nome: "João Silva",
  email: "joao@email.com",
  enderecos: [
    {
      tipo: "residencial",
      rua: "Rua A, 123",
      cidade: "São Paulo",
      cep: "01000-000",
      principal: true
    },
    {
      tipo: "comercial", 
      rua: "Av. B, 456",
      cidade: "São Paulo",
      cep: "02000-000",
      principal: false
    }
  ],
  telefones: [
    { tipo: "celular", numero: "11999999999", principal: true },
    { tipo: "fixo", numero: "1133333333", principal: false }
  ]
}
```

#### **Desvantagens do Embedding:**

- ❌ **Documento grande** (limite 16MB)
- ❌ **Duplicação** de dados se reutilizado
- ❌ **Difícil** de consultar dados aninhados independentemente
- ❌ **Crescimento** ilimitado pode ser problemático

---

### 🔗 **Referência (Normalização)**

Armazenar relacionamentos através de **IDs** em documentos separados.

#### ✅ **Quando Usar Referência:**

- Relação **1:muitos** ou **muitos:muitos**
- Dados filhos consultados **independentemente**
- **Evitar duplicação** de dados
- Dados filhos têm **ciclo de vida independente**
- **Documento pai** ficaria muito grande

#### **Exemplo Prático - Blog:**

```javascript
// Collection: users
{
  _id: ObjectId("user1"),
  nome: "João Autor",
  email: "joao@blog.com",
  bio: "Escritor apaixonado por tecnologia"
}

// Collection: posts  
{
  _id: ObjectId("post1"),
  titulo: "Introdução ao MongoDB",
  conteudo: "MongoDB é um banco de dados...",
  autor_id: ObjectId("user1"),  // 👈 REFERÊNCIA
  data_publicacao: new Date(),
  tags: ["mongodb", "nosql", "database"],
  visualizacoes: 1250
}

// Collection: comentarios
{
  _id: ObjectId("comment1"),
  post_id: ObjectId("post1"),   // 👈 REFERÊNCIA
  autor_id: ObjectId("user2"),  // 👈 REFERÊNCIA
  conteudo: "Excelente artigo!",
  data_comentario: new Date()
}
```

#### **Desvantagens da Referência:**

- ❌ **Múltiplas queries** ou `$lookup` (JOIN)
- ❌ **Sem atomicidade** entre documentos
- ❌ **Complexidade** maior no código
- ❌ **Performance** pode ser menor para leituras

---

## 🎨 **Padrões de Design Comuns**

### 1. **One-to-One (1:1)**

```javascript
// ✅ EMBEDDING - Dados sempre juntos
{
  _id: ObjectId("..."),
  nome: "João Silva",
  perfil: {
    bio: "Desenvolvedor Backend",
    avatar: "https://...",
    linkedin: "https://linkedin.com/in/joao",
    github: "https://github.com/joao"
  }
}

// ⚠️ REFERÊNCIA - Apenas se perfil for muito grande
// users collection
{ _id: ObjectId("user1"), nome: "João Silva" }

// profiles collection  
{ _id: ObjectId("profile1"), user_id: ObjectId("user1"), bio: "..." }
```

### 2. **One-to-Few (1:poucos)**

```javascript
// ✅ EMBEDDING - Até ~100 itens relacionados
{
  _id: ObjectId("..."),
  titulo: "Curso MongoDB",
  modulos: [
    {
      numero: 1,
      titulo: "Introdução",
      duracao_minutos: 45,
      videos: ["intro.mp4", "conceitos.mp4"]
    },
    {
      numero: 2, 
      titulo: "Schema Design",
      duracao_minutos: 60,
      videos: ["embedding.mp4", "referencias.mp4"]
    }
  ]
}
```

### 3. **One-to-Many (1:muitos)**

```javascript
// ⚠️ HÍBRIDO - Embedding + Referência

// products collection
{
  _id: ObjectId("product1"),
  nome: "iPhone 15",
  preco: 1200,
  // Embedding para poucas reviews destacadas
  reviews_featured: [
    {
      autor: "João",
      nota: 5,
      comentario: "Excelente produto!",
      data: new Date()
    }
  ],
  // Estatísticas agregadas
  reviews_stats: {
    total: 1534,
    media: 4.2,
    distribuicao: { 5: 800, 4: 400, 3: 200, 2: 100, 1: 34 }
  }
}

// reviews collection - Para todas as reviews
{
  _id: ObjectId("review1"),
  product_id: ObjectId("product1"),
  autor_id: ObjectId("user123"),
  nota: 5,
  comentario: "Produto chegou rápido e funcionando perfeitamente...",
  data: new Date(),
  util_count: 15
}
```

### 4. **Many-to-Many (muitos:muitos)**

```javascript
// 🔗 REFERÊNCIA - Sempre usar referências

// users collection
{
  _id: ObjectId("user1"),
  nome: "João Silva",
  // Array de IDs dos cursos
  cursos_matriculados: [
    ObjectId("curso1"),
    ObjectId("curso2")
  ]
}

// courses collection
{
  _id: ObjectId("curso1"),
  titulo: "MongoDB Avançado",
  instrutor: "Maria Santos",
  // Array de IDs dos alunos
  alunos: [
    ObjectId("user1"),
    ObjectId("user2")
  ]
}

// enrollments collection (Tabela de junção com metadados)
{
  _id: ObjectId("..."),
  user_id: ObjectId("user1"),
  course_id: ObjectId("curso1"),
  data_matricula: new Date(),
  progresso: 45, //
}
