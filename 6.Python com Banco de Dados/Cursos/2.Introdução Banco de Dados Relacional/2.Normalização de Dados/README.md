# 📚 Formas Normais

As **Formas Normais** são regras de design de banco de dados que eliminam redundâncias e anomalias, garantindo integridade e eficiência dos dados.

## 🎯 **1ª Forma Normal (1FN) - Atomicidade dos Dados**

### **Regra:** Cada campo deve conter apenas **valores atômicos** (indivisíveis)

#### ❌ **Violação da 1FN:**

```sql
CREATE TABLE usuarios_violacao (
    id INT,
    nome VARCHAR(100),
    telefones VARCHAR(200)  -- "11999999999, 1133333333" (múltiplos valores)
);
```

#### ✅ **Conformidade com 1FN:**

```sql
CREATE TABLE usuarios (
    id INT,
    nome VARCHAR(100),
    telefone VARCHAR(15)    -- Um telefone por registro
);

-- OU criar tabela separada
CREATE TABLE telefones (
    id INT,
    usuario_id INT,
    numero VARCHAR(15)
);
```

## 🎯 **2ª Forma Normal (2FN) - Dependência Funcional Total**

### **Regra:** Estar em **1FN** + eliminar **dependências parciais** da chave primária

#### ❌ **Violação da 2FN:**

```sql
CREATE TABLE pedido_produto (
    pedido_id INT,           -- Chave composta
    produto_id INT,          -- Chave composta  
    nome_produto VARCHAR(100), -- Depende apenas de produto_id (dependência parcial)
    quantidade INT,
    PRIMARY KEY (pedido_id, produto_id)
);
```

#### ✅ **Conformidade com 2FN:**

```sql
CREATE TABLE pedidos (
    id INT PRIMARY KEY,
    data_pedido DATE
);

CREATE TABLE produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100)        -- Movido para tabela própria
);

CREATE TABLE pedido_produtos (
    pedido_id INT,
    produto_id INT,
    quantidade INT,          -- Depende da chave completa
    PRIMARY KEY (pedido_id, produto_id)
);
```

## 🎯 **3ª Forma Normal (3FN) - Eliminação de Dependências Transitivas**

### **Regra:** Estar em **2FN** + eliminar **dependências transitivas**

#### ❌ **Violação da 3FN:**

```sql
CREATE TABLE funcionarios (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    departamento_id INT,
    nome_departamento VARCHAR(100)  -- Depende de departamento_id (transitiva)
);
```

#### ✅ **Conformidade com 3FN:**

```sql
CREATE TABLE departamentos (
    id INT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE funcionarios (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);
```

## 🏗️ **Análise do Modelo do Sistema de Reservas**

### ✅ **1FN Implementada com Sucesso**

**Problema Identificado:** Campo `ED_USUARIO` continha múltiplos valores concatenados:

```sql
ED_USUARIO VARCHAR(255) -- "Rua A, 123, Cidade A, Estado B"
```

**Solução Aplicada:** Divisão em campos atômicos:

```sql
NO_RUA VARCHAR(100)      -- "Rua A"
NR_ENDERECO VARCHAR(10)  -- "123"  
NO_CIDADE VARCHAR(50)    -- "Cidade A"
NO_ESTADO VARCHAR(20)    -- "Estado B"
```

### 🎯 **Status Final da Normalização:**

#### ✅ **1FN - APLICADA**

- **Migração completa** de dados concatenados
- **Campos atômicos** implementados
- **Integridade mantida** durante a transformação

#### ✅ **2FN - Não necessária**

- Todas as tabelas têm chave primária simples
- Não existem dependências parciais

#### ✅ **3FN - Não necessária**  

- Não existem dependências transitivas
- Relacionamentos via Foreign Keys corretos

## 📊 **Resumo das Formas Normais**

| Forma Normal | Elimina | Exemplo |
|--------------|---------|---------|
| **1FN** | Valores múltiplos | "João, Maria" → Registros separados |
| **2FN** | Dependências parciais | Chave composta → Dependência total |
| **3FN** | Dependências transitivas | A→B→C → A→B e B→C em tabelas separadas |

## 🏆 **Conclusão**

Nosso modelo de **Sistema de Reservas** já está adequadamente normalizado devido à sua **simplicidade e design correto**:

- ✅ **1FN**: Todos os campos são atômicos
- ✅ **2FN**: Não aplicável (chaves simples)  
- ✅ **3FN**: Não aplicável (sem dependências transitivas)

**O modelo está otimizado e segue as melhores práticas de normalização!** 🎉

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 06 - Python com Banco de Dados  
**📝 Tópico:** Normalização de Dados  
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa
