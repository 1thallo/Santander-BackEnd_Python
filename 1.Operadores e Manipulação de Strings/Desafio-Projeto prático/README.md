# Desafio - 🏦 Sistema Bancário Simples

Projeto prático desenvolvido como desafio do módulo **"Operadores e Manipulação de Strings"** do curso Santander Back-End Python na DIO.

## 📋 Descrição do Desafio

Desenvolver um sistema bancário simples em Python que simule as operações básicas de um banco, aplicando os conceitos aprendidos sobre:

- Operadores aritméticos e lógicos
- Manipulação de strings
- Estruturas condicionais
- Estruturas de repetição
- Formatação de valores

## ⚙️ Funcionalidades

### 💰 Depósito

- Permite realizar depósitos de valores positivos
- Atualiza o saldo da conta
- Registra a movimentação no extrato

### 💸 Saque

- **Limite diário**: 3 saques por dia
- **Valor máximo**: R$ 500,00 por saque
- Verificação de saldo suficiente
- Atualização automática do saldo
- Registro da movimentação no extrato

### 📄 Extrato

- Exibe todas as movimentações realizadas
- Mostra o saldo atual da conta
- Formatação monetária (R$ XX,XX)

### 🚪 Sair

- Encerra o sistema com mensagem de despedida

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+** (utiliza `match case`)
- Manipulação de strings com f-strings
- Operadores aritméticos e de comparação
- Estruturas condicionais (`match case`)
- Loops (`while`)

## 💻 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Santander-BackEnd_Python.git
```

2. Navegue até o diretório:

```bash
cd "Santander-BackEnd_Python/1.Operadores e Manipulação de Strings/Desafio-Projeto prático"
```

3. Execute o sistema:

```bash
python sistema_bancario.py
```

## 🎯 Demonstração

```
-------- BANCO ITHALLO --------

[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair

Digite sua opção: 1
Insira o valor do depósito: 100

Depósito realizado ✅! 
Saldo atual: R$ 100.00
```

## 📚 Conceitos Aplicados

### Operadores

- **Aritméticos**: `+=`, `-=` para atualização de saldo
- **Comparação**: `<=`, `>=`, `>` para validações
- **Lógicos**: `and` para múltiplas condições

### Manipulação de Strings

- **f-strings**: Formatação de valores monetários
- **Concatenação**: Construção do extrato
- **Formatação**: `.2f` para duas casas decimais

### Estruturas de Controle

- **match case**: Menu de opções (Python 3.10+)
- **if/elif/else**: Validações condicionais
- **while True**: Loop principal do sistema

## 🔧 Regras de Negócio

| Operação | Regra |
|----------|-------|
| Depósito | Valor deve ser positivo e menor que R$ 500 |
| Saque    | Máximo 3 saques/dia, valor ≤ R$ 500 e ≤ saldo |
| Extrato  | Histórico completo + saldo atual |

## 🎓 Aprendizados

Este projeto consolidou conhecimentos sobre:

- Validação de entrada de dados
- Formatação de valores monetários
- Controle de fluxo com estruturas condicionais
- Manipulação de strings para relatórios
- Uso de constantes para regras de negócio

---

**Desenvolvido por:** Ithallo  Leandro R. Barbosa
**Curso:** Santander Back-End Python  
**Módulo:** Operadores e Manipulação de Strings
