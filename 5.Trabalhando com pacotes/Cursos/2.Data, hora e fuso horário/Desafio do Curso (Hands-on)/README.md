# 🏦 Sistema Bancário com Limite Diário

Sistema bancário simples que implementa **controle de limite diário de transações** com registro detalhado de data e hora, desenvolvido para demonstrar o uso prático da biblioteca `datetime` em Python.

## 🎯 Funcionalidades Implementadas

### ✅ **Limite de 10 Transações Diárias**

- Sistema conta automaticamente as transações realizadas no dia atual
- Bloqueia novas operações quando o limite de 10 transações é atingido
- Contador é resetado automaticamente no próximo dia

### ✅ **Aviso de Limite Atingido**

- Mensagem clara e informativa quando o usuário tenta fazer a 11ª transação
- Exibição do status atual: "Transações hoje: X/10"
- Bloqueio preventivo de operações desnecessárias

### ✅ **Extrato com Data e Hora**

- Cada transação registra automaticamente data e hora completa
- Formato brasileiro padrão: `dd/mm/yyyy hh:mm:ss`
- Histórico completo de todas as operações realizadas

## 💻 Como Usar

### **Execução:**

```bash
python sistema_limite_diario.py
```

## 📊 Exemplo de Saída

### **Limite Atingido:**

```plaintext
⚠️ LIMITE ATINGIDO: Você já realizou 10 transações hoje!
```

### **Extrato Completo:**

```plaintext
==================================================
        EXTRATO - João Silva
==================================================
 1. 17/01/2025 14:30:15 | Depósito | R$    50.00
 2. 17/01/2025 14:30:16 | Saque    | R$    25.00
 3. 17/01/2025 14:30:17 | Depósito | R$    50.00
...
10. 17/01/2025 14:30:24 | Saque    | R$    25.00
--------------------------------------------------
Saldo atual: R$ 1125.00
Transações hoje: 10/10
==================================================
```

## 🔧 Recursos Técnicos

### **Controle de Data:**

- `datetime.now()` para timestamp atual
- `date()` para comparação de dias
- Formatação brasileira com `strftime()`

### **Validações:**

- Verificação de limite diário antes de cada transação
- Validação de saldo para saques
- Tratamento de valores inválidos

## 🎓 Conceitos Demonstrados

- **Datetime em Python**: Manipulação e formatação de datas
- **Controle de fluxo**: Validações e condições
- **Estruturas de dados**: Listas e dicionários para histórico
- **Interface de usuário**: Menu interativo simples

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 05 - Trabalhando com Pacotes  
**📅 Tópico:** Data, Hora e Fuso Horário  
**👨‍💻 Desenvolvido por:** Ithallo Leandro Rodrigues Barbosa
