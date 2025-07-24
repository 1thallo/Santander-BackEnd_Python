# 📦 Módulo 05 - Trabalhando com Pacotes

Este módulo aborda conceitos avançados de Python com foco em **pacotes**, **manipulação de arquivos**, **data e hora**, e **funcionalidades avançadas** como decoradores, iteradores e geradores aplicados em projetos práticos.

## 📚 **Conteúdo do Módulo**

### 🎯 **1. Decoradores, Iteradores e Geradores**

#### **Conceitos Abordados:**

- **Decoradores**: Modificação dinâmica de comportamento de funções
- **Geradores**: Processamento lazy com `yield` para eficiência de memória
- **Iteradores**: Implementação do protocolo iterator (`__iter__`, `__next__`)

#### **🏆 Desafio do Curso:**

Sistema bancário avançado implementando:

- ✅ **Decorador de Log** - Registro automático de transações
- ✅ **Gerador de Relatórios** - Processamento eficiente de dados
- ✅ **Iterador Personalizado** - Navegação customizada em coleções

**Arquivos principais:**

- [`models_decorado.py`](5.Trabalhando com pacotes/Cursos/1.Decoradores, iteradores e geradores/Desafio do Curso/models_decorado.py) - Classes com decoradores aplicados
- [`main_decorado.py`](5.Trabalhando com pacotes/Cursos/1.Decoradores, iteradores e geradores/Desafio do Curso/main_decorado.py) - Sistema principal com demonstrações

### 🕒 **2. Data, Hora e Fuso Horário**

#### **Conceitos Abordados:**

- **datetime**: Manipulação de datas e horários
- **strftime/strptime**: Formatação e conversão de strings
- **Fuso horário**: Trabalho com diferentes zonas horárias

#### **🏆 Desafio do Curso (Hands-on):**

Sistema bancário com **limite diário de transações**:
- ✅ **Controle temporal** - Máximo 10 transações por dia
- ✅ **Registro com timestamp** - Data/hora em cada operação
- ✅ **Validação automática** - Bloqueio ao atingir limite

**Arquivo principal:**

- [`sistema_limite_diario.py`](5.Trabalhando com pacotes/Cursos/2.Data, hora e fuso horário/Desafio do Curso (Hands-on)/sistema_limite_diario.py) - Sistema completo

### 📁 **3. Manipulação de Arquivos**

#### **Conceitos Abordados:**

- **Leitura/escrita** de arquivos
- **Gerenciamento** de diretórios
- **Context managers** (`with` statement)
- **Encoding** e tratamento de caracteres especiais

#### **🏆 Desafio do Curso (Hands-on):**

Sistema de **logging em arquivo**:

- ✅ **Decorador de log** - Salvamento automático em arquivo
- ✅ **Informações completas** - Data, função, argumentos, retorno
- ✅ **Persistência** - Histórico mantido entre execuções
- ✅ **Gerenciamento** - Visualização e limpeza de logs

## 📊 **Arquivos de Estudo e Exemplos**

### **Formatação e Conversão:**

- [`formatacao_conversao.py`](5.Trabalhando com pacotes/Cursos/2.Data, hora e fuso horário/formatacao_conversao.py) - Exemplos práticos de datetime

### **Manipulação de Arquivos:**

- [`leitura_arquivo.py`](5.Trabalhando com pacotes/Cursos/3.Manipulação de Arquivos/leitura_arquivo.py) - Técnicas de leitura
- [`gerenciamento_arquivos.py`](5.Trabalhando com pacotes/Cursos/3.Manipulação de Arquivos/3.gerenciamento_arquivos.py) - Operações com arquivos/diretórios
- [`lorem.txt`](5.Trabalhando com pacotes/Cursos/3.Manipulação de Arquivos/lorem.txt) - Arquivo de exemplo para testes

## 🎯 **Funcionalidades Desenvolvidas**

### **Sistema Bancário Evolutivo:**

#### **Versão 1 - Decoradores e Geradores:**

```python
@log_transacao
def depositar(self, valor):
    # Lógica de depósito com log automático
    
def gerar_relatorio(self):
    for transacao in self.transacoes:
        yield transacao  # Processamento lazy
```

#### **Versão 2 - Controle Temporal:**

```python
def _contar_transacoes_hoje(self):
    hoje = datetime.now().date()
    return len([t for t in self.transacoes if t['data'].date() == hoje])
```

#### **Versão 3 - Logging em Arquivo:**

```python
def log_transacao(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        # Salvar em log.txt
        with open("log.txt", "a") as file:
            file.write(f"[{datetime.now()}] {func.__name__}: {resultado}\n")
        return resultado
    return wrapper
```

## 💡 **Conceitos Avançados Aplicados**

### **1. Programação Funcional:**

- **Higher-order functions** com decoradores
- **Lazy evaluation** com geradores
- **Function composition** para reutilização

### **2. Orientação a Objetos:**

- **Protocolo iterator** customizado
- **Method decorators** para logging
- **Encapsulamento** com properties

### **3. Manipulação de Dados:**

- **Streaming** de dados com geradores
- **Persistência** em arquivos
- **Serialização** de informações

## 🔧 **Estrutura dos Projetos**

### **Padrão de Organização:**

```plaintext
Desafio do Curso/
├── models_*.py          # Classes e lógica de negócio
├── main_*.py           # Interface e demonstrações
├── sistema_*.py        # Sistema completo
├── log.txt            # Arquivo de log (gerado)
└── README.md          # Documentação
```

### **Características Comuns:**

- ✅ **Interface interativa** com menu
- ✅ **Demonstrações automáticas** dos conceitos
- ✅ **Código bem documentado** e comentado
- ✅ **Tratamento de erros** adequado
- ✅ **Validações** de entrada de dados

## 🚀 **Como Executar os Projetos**

### **Decoradores e Geradores:**

```bash
cd "5.Trabalhando com pacotes/Cursos/1.Decoradores, iteradores e geradores/Desafio do Curso"
python main_decorado.py
```

### **Sistema com Limite Diário:**

```bash
cd "5.Trabalhando com pacotes/Cursos/2.Data, hora e fuso horário/Desafio do Curso (Hands-on)"
python sistema_limite_diario.py
```

### **Sistema com Log em Arquivo:**

```bash
cd "5.Trabalhando com pacotes/Cursos/3.Manipulação de Arquivos/Desafio do Curso (Hands-on)"
python main_com_log_arquivo.py
```

## 📈 **Evolução Progressiva**

| Versão | Foco Principal | Tecnologias |
|--------|---------------|-------------|
| **v1** | Decoradores e Geradores | `functools`, `yield`, `__iter__` |
| **v2** | Data e Hora | `datetime`, `strftime`, validações temporais |
| **v3** | Arquivos e Persistência | `open()`, `with`, `encoding`, `os.path` |

## 🏆 **Certificado de Conclusão**

![Certificado do Módulo 05](https://github.com/user-attachments/assets/7de4d609-6abd-41ad-a767-de8e2d9f7cbc)

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 05 - Trabalhando com Pacotes
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa
