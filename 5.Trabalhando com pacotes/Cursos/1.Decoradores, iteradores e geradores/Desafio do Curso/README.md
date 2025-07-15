# 🏆 Desafio do Curso - Decoradores, Iteradores e Geradores

Este desafio propõe a implementação de **três funcionalidades avançadas** em Python aplicadas ao sistema bancário, demonstrando conceitos fundamentais de programação como decoradores, geradores e iteradores personalizados.

## 🎯 Objetivo

Implementar funcionalidades que demonstrem o uso prático de:

- **Decoradores** para logging automático
- **Geradores** para relatórios eficientes  
- **Iteradores personalizados** para navegação em coleções

## 📋 Funcionalidades Implementadas

### 🔍 1. Decorador de Log

**Objetivo:** Implementar um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

#### **Implementação:**

```python
def log_transacao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        tipo_transacao = func.__name__.replace('_', ' ').title()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[LOG] {data_hora} - Ação: {tipo_transacao}")
        return resultado
    return wrapper
```

#### **Aplicação:**

- ✅ **`@log_transacao`** aplicado em `depositar()`, `sacar()`, `criar_cliente()`, `criar_conta()`
- ✅ **Registro automático** de data/hora e tipo de operação
- ✅ **Não invasivo** - não altera o código das funções originais
- ✅ **`functools.wraps`** preserva metadados da função original

#### **Resultado:**

```plaintext
[LOG] 15/01/2025 14:30:15 - Ação: Criar Cliente
[LOG] 15/01/2025 14:30:16 - Ação: Depositar
[LOG] 15/01/2025 14:30:17 - Ação: Sacar
```

### 📊 2. Gerador de Relatório

**Objetivo:** Criar um gerador que permita iterar sobre as transações de uma conta corrente e retorne, uma a uma, as transações que forem realizadas. Deve também ter uma forma de filtrar as transações baseado em seu tipo (exemplo, apenas saques ou apenas depósitos).

#### **Implementação:**

```python
class GeradorRelatorio:
    def gerar_todas_transacoes(self):
        """Gerador que retorna todas as transações uma por vez"""
        for transacao in self.conta.transacoes:
            yield transacao
    
    def gerar_por_tipo(self, tipo_filtro):
        """Gerador que filtra transações por tipo"""
        for transacao in self.conta.transacoes:
            if transacao['tipo'].lower() == tipo_filtro.lower():
                yield transacao
```

#### **Características:**

- ✅ **Lazy evaluation** - não carrega todas as transações na memória
- ✅ **Filtragem por tipo** - depósitos, saques ou todos
- ✅ **Memory efficient** - ideal para grandes volumes de dados
- ✅ **Interface simples** - fácil de usar com `for` loops

#### **Exemplo de Uso:**

```python
gerador = GeradorRelatorio(conta)

# Todas as transações
for transacao in gerador.gerar_todas_transacoes():
    print(f"{transacao['tipo']}: R$ {transacao['valor']:.2f}")

# Apenas depósitos
for deposito in gerador.gerar_por_tipo('Depósito'):
    print(f"Depósito: R$ {deposito['valor']:.2f}")
```

### 🔄 3. Iterador Personalizado

**Objetivo:** Implementar um iterador personalizado `ContaIterador` que permite iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc.)

#### **Implementação:**

```python
class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self.indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice >= len(self.contas):
            raise StopIteration
        
        conta = self.contas[self.indice]
        info_conta = {
            'numero': conta.numero,
            'titular': conta.cliente.nome,
            'cpf': conta.cliente.cpf,
            'saldo': conta.saldo,
            'qtd_transacoes': len(conta.transacoes)
        }
        
        self.indice += 1
        return info_conta
```

#### **Características:**

- ✅ **Protocolo Iterator** - implementa `__iter__()` e `__next__()`
- ✅ **Informações completas** - número, titular, CPF, saldo, quantidade de transações
- ✅ **Compatível com `for`** - pode ser usado em loops nativos
- ✅ **Controle de estado** - mantém posição atual da iteração

#### **Exemplo de Uso:**

```python
iterador = ContaIterador(banco.contas)

for info in iterador:
    print(f"Conta {info['numero']}: {info['titular']} - R$ {info['saldo']:.2f}")
```

## 🏗️ Arquitetura da Solução

### **Estrutura de Arquivos:**

```plaintext
Desafio do Curso/
├── models_decorado.py    # Classes com decoradores aplicados
├── main_decorado.py      # Interface principal e demonstrações
└── README.md             # Documentação (este arquivo)
```

### **Classes Principais:**

- **`Cliente`**: Gerencia informações pessoais e contas
- **`Conta`**: Operações bancárias com logging automático
- **`Banco`**: Coordena clientes e contas
- **`GeradorRelatorio`**: Gera relatórios sob demanda
- **`ContaIterador`**: Navega através das contas

## 🎮 Funcionalidades do Sistema

### **1. Demonstrações Automáticas**

- ✅ **Decoradores em ação** - logs automáticos de todas as operações
- ✅ **Gerador de relatórios** - diferentes tipos de filtros
- ✅ **Iterador de contas** - navegação completa

### **2. Menu Interativo**

- ✅ **Realizar Depósito** - com logging automático
- ✅ **Realizar Saque** - com validações e logs
- ✅ **Ver Relatórios** - usando geradores
- ✅ **Listar Contas** - usando iterador personalizado

## 🚀 Como Executar

```bash
python main_decorado.py
```

## 📊 Exemplo de Saída Completa

```plaintext
🚀 INICIANDO DEMONSTRAÇÕES
==================================================
    🎯 DEMONSTRAÇÃO DE DECORADORES
==================================================
[LOG] 15/01/2025 14:30:15 - Ação: Criar Cliente 
✅ Cliente João Silva criado com sucesso!
[LOG] 15/01/2025 14:30:15 - Ação: Criar Cliente 
✅ Cliente Maria Santos criado com sucesso!

[LOG] 15/01/2025 14:30:15 - Ação: Criar Conta 
✅ Conta 1 criada para João Silva!
[LOG] 15/01/2025 14:30:15 - Ação: Criar Conta 
✅ Conta 2 criada para Maria Santos!

[LOG] 15/01/2025 14:30:15 - Ação: Depositar 
✅ Depósito de R$ 1000.00 realizado com sucesso!
[LOG] 15/01/2025 14:30:15 - Ação: Sacar 
✅ Saque de R$ 250.00 realizado com sucesso!

🎯 DEMONSTRAÇÃO DO GERADOR DE RELATÓRIOS
==================================================
📊 Relatório da Conta 1 - João Silva
----------------------------------------

📋 TODAS AS TRANSAÇÕES:
1. Depósito | R$  1000.00 | 15/01/2025 14:30:15
2. Saque    | R$   250.00 | 15/01/2025 14:30:15
3. Depósito | R$   500.00 | 15/01/2025 14:30:15

💰 APENAS DEPÓSITOS:
1. R$  1000.00 | 15/01/2025 14:30:15
2. R$   500.00 | 15/01/2025 14:30:15

💸 APENAS SAQUES:
1. R$   250.00 | 15/01/2025 14:30:15

🎯 DEMONSTRAÇÃO DO ITERADOR DE CONTAS
==================================================
🏦 INFORMAÇÕES DAS CONTAS:
----------------------------------------
Conta:   1 | Titular: João Silva      | CPF: 12345678901 | Saldo: R$  1250.00 | Transações: 3
Conta:   2 | Titular: Maria Santos    | CPF: 98765432100 | Saldo: R$   650.00 | Transações: 2
```

## 💡 Conceitos Demonstrados

### **1. Decoradores**

- **Aspect-Oriented Programming**: Separação de concerns (logging vs lógica de negócio)
- **Metaprogramming**: Modificação dinâmica do comportamento
- **`functools.wraps`**: Preservação de metadados

### **2. Geradores**

- **Lazy Evaluation**: Processamento sob demanda
- **Memory Efficiency**: Ideal para grandes datasets
- **`yield`**: Pausa e resume da execução

### **3. Iteradores**

- **Iterator Protocol**: `__iter__()` e `__next__()`
- **State Management**: Controle da posição atual
- **Custom Iteration**: Lógica personalizada de navegação

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 05 - Trabalhando com Pacotes  
**📝 Desafio:** Decoradores, Iteradores e Geradores  
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa
