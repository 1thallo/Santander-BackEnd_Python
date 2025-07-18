# 🏆 Desafio do Curso - Manipulação de Arquivos

Sistema de **logging em arquivo** implementado através de decorador Python, aplicado ao sistema bancário para demonstrar o uso prático de manipulação de arquivos com registro detalhado de operações.

## 🎯 Objetivo

Modificar o decorador de log existente para salvar informações detalhadas em um arquivo de texto, mantendo um histórico persistente de todas as operações realizadas no sistema.

## 📋 Funcionalidades Implementadas

### ✅ **Decorador de Log para Arquivo**

- **Registro automático** de todas as funções decoradas
- **Salvamento em arquivo** `log.txt`
- **Append mode** - novos logs adicionados ao final
- **Uma linha por entrada** com informações completas

### ✅ **Informações Registradas**

Cada entrada de log contém:

- ✅ **Data e hora atuais** (formato brasileiro: dd/mm/yyyy hh:mm:ss)
- ✅ **Nome da função** executada
- ✅ **Argumentos da função** (valores e tipos)
- ✅ **Valor retornado** pela função

### ✅ **Método `__repr__` Implementado**

Todas as classes possuem representação clara:

- **Cliente**: `Cliente: ('12345678901')`
- **Conta**: `ContaCorrente: ('1')`
- **Banco**: `Banco: ('Banco Ithallo')`
- **Iterador**: `ContaIterador: (2 contas)`

## 📊 Exemplo do Arquivo log.txt

```plaintext
[17/01/2025 15:30:15] Função: criar_cliente | Argumentos: arg1=João Silva, arg2=12345678901 | Retorno: Cliente: ('12345678901')
[17/01/2025 15:30:16] Função: criar_conta | Argumentos: arg1=Cliente: ('12345678901'), arg2=corrente | Retorno: ContaCorrente: ('1')
[17/01/2025 15:30:16] Função: depositar | Argumentos: arg1=1000.0 | Retorno: True
[17/01/2025 15:30:17] Função: sacar | Argumentos: arg1=250.0 | Retorno: True
```

## 🔧 Implementação Técnica

### **Decorador de Log:**

```python
def log_transacao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        
        # Capturar informações
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        nome_funcao = func.__name__
        args_str = preparar_argumentos(args, kwargs)
        
        # Salvar no arquivo
        linha_log = f"[{data_hora}] Função: {nome_funcao} | Argumentos: {args_str} | Retorno: {resultado}\n"
        
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(linha_log)
        
        return resultado
    return wrapper
```

### **Gerenciamento de Log:**

- **Ler log**: Visualização completa do histórico
- **Limpar log**: Reset do arquivo para novos testes
- **Encoding UTF-8**: Suporte a caracteres especiais

## 🎮 Funcionalidades do Sistema

### **Menu Interativo:**

- **[1]** Realizar Depósito
- **[2]** Realizar Saque  
- **[3]** Ver Relatório de Transações
- **[4]** Listar Todas as Contas
- **[5]** 📄 Ver Arquivo de Log
- **[6]** 🗑️ Limpar Arquivo de Log
- **[7]** 🧪 Teste Rápido (5 transações)

### **Demonstrações Automáticas:**

- ✅ Criação de clientes e contas (com log)
- ✅ Operações bancárias diversas (com log)
- ✅ Geração de relatórios
- ✅ Navegação por iterador personalizado

## 🚀 Como Executar

```bash
python main_com_log_arquivo.py
```

## 📁 Arquivos Gerados

### **log.txt**

- Arquivo principal de log
- Criado automaticamente na primeira execução
- Novos logs adicionados continuamente
- Persistente entre execuções

## 🎯 Requisitos Atendidos

| Requisito | Status | Implementação |
|-----------|--------|---------------|
| Data e hora atuais | ✅ | `datetime.now().strftime()` |
| Nome da função | ✅ | `func.__name__` |
| Argumentos da função | ✅ | Parsing de `*args` e `**kwargs` |
| Valor retornado | ✅ | Captura do `resultado` |
| Arquivo log.txt | ✅ | `open("log.txt", "a")` |
| Append mode | ✅ | Modo `"a"` para adicionar |
| Uma linha por entrada | ✅ | `\n` ao final de cada log |

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 05 - Trabalhando com Pacotes  
**📝 Tópico:** Manipulação de Arquivos  
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa  
