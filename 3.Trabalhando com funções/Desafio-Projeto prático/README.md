# 🏦 Sistema Bancário com Funções - Versão Otimizada

Evolução do sistema bancário simples, agora implementado com **funções modulares** e **recursos** de cadastro de usuários e contas.

## 🎯 Objetivo do Projeto

Refatorar o sistema bancário original aplicando conceitos de **programação funcional** e **modularização**, implementando:

- ✅ Funções de **saque**, **depósito** e **extrato**
- ✅ Sistema de **cadastro de usuários**
- ✅ Criação de **contas bancárias** vinculadas
- ✅ **Listagem** de usuários e contas
- ✅ **Validações** e regras de negócio aprimoradas

## Certificado de Conclusão

![Certificado](https://github.com/user-attachments/assets/2bf49ac9-5d00-420c-ac12-813bac67272c)

## 🔧 Funcionalidades Implementadas

### 💸 Operações Bancárias

#### **Saque**

- **Argumentos**: Apenas por palavra-chave (`keyword-only`)
- **Parâmetros**: `saldo`, `valor`, `extrato`, `numero_saques`, `limite_saques`, `limite_valor`
- **Validações**: Limite diário, valor máximo, saldo suficiente
- **Retorno**: `saldo` e `extrato` atualizados

#### **Depósito**

- **Argumentos**: Apenas por posição (`positional-only`)
- **Parâmetros**: `saldo`, `valor`, `extrato`
- **Validações**: Valor positivo
- **Retorno**: `saldo` e `extrato` atualizados

#### **Extrato**

- **Argumentos**: Mistos (posicionais e nomeados)
- **Posicionais**: `saldo`
- **Nomeados**: `extrato`
- **Funcionalidade**: Exibe histórico formatado

### 👥 Gestão de Usuários

#### **Cadastro de Usuários**

```python
usuario = {
    "nome": "João Silva",
    "data_nascimento": "15/03/1990", 
    "cpf": "12345678901",
    "endereco": "Rua das Flores, 123 - Centro - São Paulo/SP"
}
```

**Regras:**

- ✅ CPF único (não permite duplicatas)
- ✅ Endereço completo em string única
- ✅ Validação de dados obrigatórios

#### **Listagem de Usuários**

- Exibe todos os usuários cadastrados
- Formato organizado e legível
- Verificação de lista vazia

### 🏛️ Gestão de Contas

#### **Criação de Contas**

```python
conta = {
    "agencia": "0001",
    "numero_conta": 1,  # Sequencial
    "usuario": usuario  # Referência ao usuário
}
```

**Regras:**

- ✅ Agência fixa: **"0001"**
- ✅ Numeração sequencial: 1, 2, 3...
- ✅ Vinculação obrigatória com usuário existente
- ✅ Um usuário pode ter múltiplas contas
- ✅ Uma conta pertence a apenas um usuário

#### **Listagem de Contas**

- Exibe agência, número e titular
- Formatação clara e organizada
- Verificação de contas existentes

## 🛠️ Arquitetura do Sistema

### **Modularização**

```
📁 Projeto/
├── 📄 sistema_bancario.py      # Interface principal
├── 📄 funcoes_sistema_bancario.py  # Funções do sistema
└── 📄 README.md               # Documentação
```

### **Separação de Responsabilidades**

#### `funcoes_sistema_bancario.py`

- **Funções puras** sem efeitos colaterais
- **Validações** centralizadas
- **Reutilização** de código
- **Testabilidade** aprimorada

#### `sistema_bancario.py`

- **Interface de terminal do usuário**
- **Controle de fluxo** principal
- **Importação** de funções
- **Gerenciamento** de estado

## 💻 Como Executar

### **1. Executar o Sistema**

```bash
python sistema_bancario.py
```

### **2. Menu Principal**

```
========== BANCO ITHALLO ==========

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[7] Listar usuários
[0] Sair
```

### **3. Exemplo de Uso**

```python
# 1. Cadastrar usuário
Nome: João Silva
CPF: 12345678901
Data: 15/03/1990
Endereço: Rua das Flores, 123 - Centro - São Paulo/SP

# 2. Criar conta
CPF: 12345678901
✅ Conta criada! Agência: 0001, Conta: 1

# 3. Realizar operações
Depósito: R$ 1000.00
Saque: R$ 500.00
```

## 🎯 Conceitos Aplicados

### **Estruturas de Dados**

- **Listas**: Armazenamento de usuários e contas
- **Dicionários**: Estruturação de dados complexos
- **Strings**: Formatação e validação de dados

### **Programação Funcional**

- **Funções puras**: Sem efeitos colaterais
- **Immutabilidade**: Dados não alterados diretamente
- **Composição**: Funções que trabalham em conjunto

## 🔍 Validações Implementadas

### **Operações Bancárias**

| Validação | Saque | Depósito |
|-----------|-------|----------|
| Valor positivo | ✅ | ✅ |
| Saldo suficiente | ✅ | - |
| Limite diário | ✅ | - |
| Valor máximo | ✅ | - |

### **Gestão de Dados**

| Validação | Usuário | Conta |
|-----------|---------|-------|
| CPF único | ✅ | - |
| Usuário existente | - | ✅ |
| Dados obrigatórios | ✅ | ✅ |

## 📊 Melhorias Implementadas

### **Comparação com Versão Anterior**

| Aspecto | Versão 1 | Versão 2 (Atual) |
|---------|----------|-------------------|
| **Estrutura** | Monolítica | Modular |
| **Funções** | Inline | Separadas |
| **Usuários** | ❌ | ✅ |
| **Contas** | ❌ | ✅ |
| **Validações** | Básicas | Avançadas |
| **Reutilização** | Baixa | Alta |
| **Testabilidade** | Difícil | Fácil |

### **Benefícios da Refatoração**

- 🔄 **Reutilização**: Funções podem ser usadas independentemente
- 🧪 **Testabilidade**: Cada função pode ser testada isoladamente
- 📖 **Legibilidade**: Código mais organizado e compreensível
- 🔧 **Manutenibilidade**: Mais fácil de atualizar e corrigir
- 📈 **Escalabilidade**: Base sólida para futuras funcionalidades

### **Boas Práticas**

- Separação de responsabilidades
- Código modular e reutilizável
- Validações consistentes
- Interface de usuário intuitiva

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 03 - Trabalhando com Funções  
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa  
**🔄 Versão:** 2.0 - Sistema Otimizado com Funções
