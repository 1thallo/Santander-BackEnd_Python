# ⚙️ Módulo 03 - Trabalhando com Funções

Este módulo aprofunda os conceitos de **programação funcional** em Python, explorando desde funções básicas até implementações avançadas com diferentes tipos de argumentos e modularização de código.

## Certificado de Conclusão do Módulo 03

![Certificado](https://github.com/user-attachments/assets/b9f013d9-320b-44f1-8fb0-8b16dee9c36f)

## 📖 Conteúdo do Módulo

### 🔧 1. Fundamentos de Funções

#### Conceitos Básicos

- **Definição**: `def nome_funcao():`
- **Parâmetros e argumentos**: Valores de entrada
- **Argumentos padrão**: Valores default
- **Retorno**: `return` para devolver valores
- **Docstrings**: Documentação de funções

### 🔄 2. Retorno de Valores

#### Tipos de Retorno

- **Retorno único**: Um valor específico
- **Retorno múltiplo**: Tupla com múltiplos valores
- **Sem return**: Função retorna `None`

### 🏷️ 3. Argumentos Nomeados

#### Formas de Passagem

- **Posicionais**: `funcao(valor1, valor2)`
- **Nomeados**: `funcao(param1=valor1, param2=valor2)`
- **Dicionário**: `funcao(**dict_argumentos)`

### 📦 4. *args e **kwargs

#### Argumentos Variáveis

- **`*args`**: Argumentos posicionais variáveis (tupla)
- **`**kwargs`**: Argumentos nomeados variáveis (dicionário)
- **Flexibilidade**: Aceita qualquer quantidade de argumentos

### 🎯 5. Parâmetros Especiais

#### Tipos de Restrição

```python
def funcao(pos1, pos2, /, pos_or_keyword, *, keyword1, keyword2):
    pass
```

##### Restrições Disponíveis

- **Apenas Posicional (`/`)**: Parâmetros só por posição
- **Apenas Palavra-chave (`*`)**: Parâmetros só nomeados
- **Combinação**: Máxima flexibilidade e controle

### 🎪 6. Funções de Primeira Classe

#### Características

- **Primeira classe**: Funções são objetos como qualquer outro
- **Passagem como argumento**: Funções podem ser parâmetros
- **Flexibilidade**: Permite programação funcional avançada

### 🌐 7. Escopo de Variáveis

#### Regras de Escopo

- **Local**: Variáveis dentro da função
- **Global**: Variáveis fora de todas as funções
- **`global`**: Palavra-chave para modificar variáveis globais
- **LEGB**: Local → Enclosing → Global → Built-in

## 🎯 Projetos Práticos

### 🏥 [Sistema de Atendimento Médico](./Desafio-Código/sistema_atendimento_medico.py)

**Conceitos aplicados:**

- Funções com lógica complexa de priorização
- Ordenação customizada com `key`
- Manipulação de estruturas de dados

**Regras implementadas:**

- Pacientes urgentes: prioridade máxima (por idade)
- Pacientes ≥60 anos: segunda prioridade
- Demais: ordem de chegada

### 🏨 [Sistema de Reserva de Hotel](./Desafio-Código/sistema_reserva_hotel.py)

**Conceitos aplicados:**

- Uso de `set()` para verificação eficiente
- Processamento sequencial de listas
- Validação de disponibilidade

### 🏦 [Sistema Bancário Otimizado](./Desafio-Projeto%20prático/)

**Arquitetura modular:**

- `funcoes_sistema_bancario.py`: Funções puras e reutilizáveis
- `sistema_bancario.py`: Interface e controle de fluxo

**Funcionalidades:**

- Operações bancárias (saque, depósito, extrato)
- Gestão de usuários e contas
- Validações avançadas

**Tipos de argumentos implementados:**

- `keyword-only` para operações críticas
- `positional-only` para dados básicos
- Argumentos mistos para flexibilidade

## 📂 Estrutura do Diretório

```plaintext
3.Trabalhando com funções/
├── Cursos/
│   └── 1.Funções/
│       ├── funcoes_pt01.py
│       ├── funcoes_pt02.py
│       └── README.md (certificado)
├── Desafio-Código/
│   ├── sistema_atendimento_medico.py
│   └── sistema_reserva_hotel.py
├── Desafio-Projeto prático/
│   ├── funcoes_sistema_bancario.py
│   ├── sistema_bancario.py
│   └── README.md
└── README.md (este arquivo)
```

## 🎓 Objetivos de Aprendizagem

Habilidades desenvolvidas:

- ✅ **Criar funções** com diferentes tipos de parâmetros
- ✅ **Implementar argumentos** posicionais, nomeados e variáveis
- ✅ **Aplicar restrições** de argumentos (`/` e `*`)
- ✅ **Usar funções** como objetos de primeira classe
- ✅ **Gerenciar escopo** de variáveis
- ✅ **Modularizar código**
- ✅ **Implementar validações** e regras de negócio

## 💡 Boas Práticas Consolidadas

### **Design de Funções:**

- Uma responsabilidade por função
- Nomes descritivos e verbos de ação
- Documentação com docstrings
- Funções puras sem efeitos colaterais

### **Modularização:**

- Separar lógica de negócio da interface
- Imports específicos
- Testabilidade aprimorada

## 📊 Benefícios da Abordagem Funcional

| Aspecto | Sem Funções | Com Funções |
|---------|-------------|-------------|
| **Reutilização** | ❌ Código duplicado | ✅ Código reutilizável |
| **Manutenção** | ❌ Difícil | ✅ Fácil |
| **Teste** | ❌ Complexo | ✅ Simples |
| **Organização** | ❌ Monolítico | ✅ Modular |

### 📜 Certificados de Conclusão

- 🏆 **[Dominando Funções Python](./Cursos/1.Funções/README.md)** - Certificado de conclusão

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 03 - Trabalhando com Funções  
**👨‍💻 Desenvolvido por:** Ithallo Leandro Rodrigues Barbosa
