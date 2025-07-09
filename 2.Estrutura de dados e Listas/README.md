# 📊 Módulo 02 - Estrutura de Dados e Listas

Este módulo explora as principais estruturas de dados em Python, fundamentais para o desenvolvimento back-end eficiente e organização de informações.

## 🏆 Certificado de Conclusão do Módulo

![Certificado de Conclusão do Módulo](https://github.com/user-attachments/assets/28691f8f-df4b-4cf8-9ccb-678f16207c89)

## 📖 Conteúdo do Módulo

### 📋 1. Listas

Estrutura de dados mutável e ordenada para armazenar múltiplos elementos.

#### Conceitos Fundamentais

- **Declaração**: `frutas = ["laranja", "maca", "uva"]`
- **Acesso direto**: `frutas[0]`, `frutas[-1]`
- **Fatiamento**: `lista[2:]`, `lista[:2]`, `lista[1:3]`
- **Listas aninhadas**: `matriz = [[1, "a", 2], ["b", 3, 4]]`
- **Iteração**: `for item in lista:`
- **Compreensão de lista**: `[x**2 for x in numeros if x % 2 == 0]`

#### Métodos Principais

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `.append()` | Adiciona elemento ao final | `lista.append("novo")` |
| `.extend()` | Adiciona múltiplos elementos | `lista.extend(["a", "b"])` |
| `.insert()` | Insere em posição específica | `lista.insert(0, "inicio")` |
| `.remove()` | Remove por valor | `lista.remove("item")` |
| `.pop()` | Remove por índice | `lista.pop(0)` |
| `.sort()` | Ordena a lista | `lista.sort(reverse=True)` |
| `.count()` | Conta ocorrências | `lista.count("item")` |

### 🔗 2. Tuplas

Estrutura de dados **imutável** e ordenada, ideal para dados que não devem ser alterados.

#### Características

- **Declaração**: `tupla = ("a", "b", "c")`
- **Imutabilidade**: Não permite alterações após criação
- **Acesso**: `tupla[0]`, `tupla[-1]`
- **Fatiamento**: `tupla[1:3]`
- **Desempacotamento**: `a, b, c = tupla`

#### Métodos Disponíveis

- `.count()`: Conta ocorrências
- `.index()`: Encontra índice do elemento
- `len()`: Retorna tamanho

### 🔢 3. Conjuntos (Sets)

Coleção **não ordenada** de elementos **únicos**, sem duplicatas.

#### Operações de Conjunto

```python
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# União
conjunto_a.union(conjunto_b)  # {1, 2, 3, 4, 5}

# Interseção
conjunto_a.intersection(conjunto_b)  # {3}

# Diferença
conjunto_a.difference(conjunto_b)  # {1, 2}

# Diferença simétrica
conjunto_a.symmetric_difference(conjunto_b)  # {1, 2, 4, 5}
```

#### Métodos de Verificação

- `.issubset()`: Verifica se é subconjunto
- `.issuperset()`: Verifica se é superconjunto
- `.isdisjoint()`: Verifica se não há elementos em comum

### 🗂️ 4. Dicionários

Estrutura de dados **mapeamento** chave-valor, fundamental para organização de dados.

#### Operações Básicas

```python
pessoa = {"nome": "João", "idade": 25}

# Acesso
pessoa["nome"]  # "João"

# Adição/Modificação
pessoa["telefone"] = "123456789"

# Iteração
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

#### Métodos Essenciais

| Método | Descrição | Exemplo |
|--------|-----------|---------|
| `.get()` | Acesso seguro | `dict.get("chave", "padrão")` |
| `.keys()` | Retorna chaves | `dict.keys()` |
| `.values()` | Retorna valores | `dict.values()` |
| `.items()` | Retorna pares chave-valor | `dict.items()` |
| `.pop()` | Remove e retorna valor | `dict.pop("chave")` |
| `.update()` | Atualiza dicionário | `dict.update({"nova": "chave"})` |

## 🎯 Projetos Práticos

### 🛒 [Simulador de Carrinho de Compras](./Desafio-Código/1.simulador_carrinho_compras.py)

Sistema que demonstra o uso de **listas** e **tuplas** para:

- Armazenar produtos e preços
- Calcular totais
- Formatar saídas monetárias

**Conceitos aplicados:**

- Manipulação de listas com `.append()`
- Tuplas para estruturar dados (produto, preço)
- Formatação de strings com `:.2f`
- Iteração e acumulação de valores

### 📅 [Organizador de Eventos](./Desafio-Código/2.organizador_eventos.py)

Sistema que utiliza **dicionários** para:

- Agrupar participantes por tema
- Organizar dados dinamicamente
- Exibir resultados formatados

**Conceitos aplicados:**

- Dicionários com listas como valores
- Verificação de existência de chaves
- Método `.items()` para iteração
- `.join()` para formatação de saída

## 🛠️ Tecnologias e Ferramentas

- **Estruturas de dados nativas**
- **Métodos built-in**
- **Compreensão de listas**
- **Manipulação de strings**

## 📂 Estrutura do Diretório

```
2.Estrutura de dados e Listas/
├── Cursos/
│   ├── 1.Listas/
│   │   ├── listas.py
│   │   └── metodos_listas.py
│       └── README.md (certificado)
│   ├── 2.Tuplas/
│   │   ├── tuplas.py
│   │   └── metodos_tuplas.py
│       └── README.md (certificado)
│   ├── 3.Conjuntos/
│   │   ├── conjuntos.py
│   │   └── metodos_conjuntos.py
│       └── README.md (certificado)
│   └── 4.Dicionários/
│       ├── dicionarios.py
│       ├── metodos_dict.py
│       └── README.md (certificado)
├── Desafio-Código/
│   ├── 1.simulador_carrinho_compras.py
│   └── 2.organizador_eventos.py
└── README.md (este arquivo)
```

### 📜 Certificados de Conclusão

Cada subdiretório de curso contém um README.md com o certificado de conclusão:

- 🏆 **[Trabalhando com Listas](./Cursos/1.Listas/README.md)** - Certificado de conclusão
- 🏆 **[Conhecendo Tuplas](./Cursos/2.Tuplas/README.md)** - Certificado de conclusão  
- 🏆 **[Explorando Conjuntos](./Cursos/3.Conjuntos/README.md)** - Certificado de conclusão
- 🏆 **[Aprendendo a Utilizar Dicionários](./Cursos/4.Dicionários/README.md)** - Certificado de conclusão

## 🎓 Objetivos de Aprendizagem

Habilidades desenvolvidas durante o módulo:

- ✅ **Manipular listas**
- ✅ **Utilizar tuplas** para dados imutáveis
- ✅ **Operar conjuntos** com álgebra de conjuntos
- ✅ **Gerenciar dicionários** para mapeamentos
- ✅ **Escolher a estrutura adequada** para cada situação

## 📊 Comparativo das Estruturas

| Estrutura | Ordenada | Mutável | Permite Duplicatas | Acesso |
|-----------|----------|---------|-------------------|--------|
| **Lista** | ✅ | ✅ | ✅ | Por índice |
| **Tupla** | ✅ | ❌ | ✅ | Por índice |
| **Conjunto** | ❌ | ✅ | ❌ | Por valor |
| **Dicionário** | ✅ (Python 3.7+) | ✅ | ❌ (chaves) | Por chave |

## 💡 Boas Práticas Consolidadas

### **Escolha da Estrutura:**

- **Lista**: Quando precisar de ordem e mutabilidade
- **Tupla**: Para dados que não devem mudar
- **Conjunto**: Para eliminar duplicatas e operações matemáticas
- **Dicionário**: Para mapeamentos e consultas rápidas

---

**📚 Curso:** Bootcamp Santander Back-End Python  
**🎯 Módulo:** 02 - Estrutura de Dados e Listas  
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa
