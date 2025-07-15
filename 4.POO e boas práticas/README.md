# 🎯 Módulo 04 - POO e Boas Práticas

Este módulo apresenta os **conceitos fundamentais da Programação Orientada a Objetos (POO)** em Python, abordando desde os princípios básicos até implementações avançadas com classes abstratas e interfaces.

## 📖 Conteúdo do Módulo

### 🔧 1. Introdução à POO

#### **Conceitos Fundamentais**

- **Classes e Objetos**: Definição de estruturas e criação de instâncias
- **Atributos e Métodos**: Características e comportamentos dos objetos
- **Construtores e Destrutores**: Métodos `__init__()` e `__del__()`
- **Representação de Objetos**: Método `__str__()` para saída personalizada

#### **Primeiros Passos**

- Criação de classes simples
- Instanciação de objetos
- Definição de métodos de comportamento
- Gerenciamento do ciclo de vida dos objetos

### 🧬 2. Conceitos de Herança

#### **Herança Simples**

- **Classe Pai (Superclasse)**: Define características comuns
- **Classes Filhas (Subclasses)**: Herdam e especializam comportamentos
- **`super()`**: Acesso aos métodos da classe pai
- **`isinstance()`**: Verificação de tipos e hierarquia

#### **Herança Múltipla**

- **MRO (Method Resolution Order)**: Ordem de resolução de métodos
- **Mixins**: Classes auxiliares para funcionalidades específicas
- **Problemas e Soluções**: Diamond problem e resolução de conflitos

#### **Reutilização de Código**

- Compartilhamento de funcionalidades comuns
- Especialização de comportamentos específicos
- Organização hierárquica de classes

### 🔒 3. Encapsulamento

#### **Controle de Acesso**

- **Atributos Públicos**: Acesso direto e livre
- **Atributos Privados**: Convenção com `_` (protected) e `__` (private)
- **Métodos de Acesso**: Getters e setters para controle

#### **Properties**

- **`@property`**: Transformar métodos em atributos
- **`@setter`**: Controlar atribuição de valores
- **`@deleter`**: Controlar remoção de atributos
- **Validações**: Implementar regras de negócio no acesso

### 🎭 4. Polimorfismo

#### **Conceitos Básicos**

- **Mesma Interface, Comportamentos Diferentes**: Métodos com mesmo nome, implementações distintas
- **Duck Typing**: "Se anda como pato e fala como pato, é um pato"
- **Sobrescrita de Métodos**: Redefinição em classes filhas

#### **Aplicações Práticas**

- Tratamento uniforme de objetos diferentes
- Extensibilidade através de interfaces comuns
- Código mais flexível e reutilizável

### 🎨 5. Interfaces e Classes Abstratas

#### **Abstract Base Classes (ABC)**

- **Módulo `abc`**: Ferramentas para abstração
- **`@abstractmethod`**: Métodos que devem ser implementados
- **Contratos de Interface**: Definição de comportamentos obrigatórios

#### **Métodos Especiais**

- **`@classmethod`**: Métodos que recebem a classe como primeiro argumento
- **`@staticmethod`**: Métodos independentes da instância ou classe
- **Factory Methods**: Padrões de criação de objetos

#### **Variáveis de Classe vs Instância**

- **Variáveis de Classe**: Compartilhadas entre todas as instâncias
- **Variáveis de Instância**: Específicas de cada objeto
- **Escopo e Visibilidade**: Diferenças de acesso e modificação

## 🎯 Projetos Práticos

### 🏦 [Sistema Bancário Orientado a Objetos](./Desafio-Projeto%20prático/)

**Evolução completa** do sistema funcional para POO com arquitetura modular:

**Características Implementadas:**

- **Hierarquia de Classes**: Cliente → PessoaFisica, Conta → ContaCorrente
- **Classes Abstratas**: Transacao com implementações Saque e Deposito
- **Encapsulamento**: Atributos privados com properties
- **Polimorfismo**: Métodos abstratos com implementações específicas

**Arquitetura Modular:**

- `models.py`: Classes do domínio bancário
- `utils.py`: Funções auxiliares e validações
- `main.py`: Interface principal e execução

### 🍕 [Sistema de Pedidos de Restaurante](./Desafio-Código/pedidos_restaurante.py)

**Conceitos Aplicados:**

- Classe simples com atributos e métodos
- Manipulação de listas e cálculos
- Formatação de saída com precisão decimal

### 🚗 [Sistema de Gestão de Veículos](./Desafio-Código/gestao_veiculos.py)

**Conceitos Aplicados:**

- Classe com lógica de negócio
- Uso de bibliotecas externas (`datetime`)
- Métodos de validação e classificação

## 📂 Estrutura do Diretório

```plaintext
4.POO e boas práticas/
├── Cursos/
│   ├── 1.Introdução a POO/
│   ├── 2.Conceitos de Herança/
│   ├── 3.Encapsulamento/
│   ├── 4.Polimorfismo/
│   └── 5.Interfaces e Classes Abstratas/
├── Desafio-Código/
│   ├── pedidos_restaurante.py
│   └── gestao_veiculos.py
├── Desafio-Projeto prático/
│   ├── models.py
│   ├── utils.py
│   ├── main.py
│   └── README.md
└── README.md (este arquivo)
```

## 🎓 Objetivos de Aprendizagem

Habilidades desenvolvidas:

- ✅ **Projetar classes** coesas e com responsabilidades bem definidas
- ✅ **Implementar herança** simples e múltipla apropriadamente
- ✅ **Aplicar encapsulamento** para proteger dados e controlar acesso
- ✅ **Utilizar polimorfismo** para código flexível e extensível
- ✅ **Criar interfaces** com classes abstratas e métodos obrigatórios
- ✅ **Organizar código** em arquiteturas modulares e escaláveis
- ✅ **Seguir boas práticas** de desenvolvimento orientado a objetos

## 💡 Benefícios da Programação Orientada a Objetos

### **Para Desenvolvimento**

- **Modularidade**: Código organizado em unidades coesas
- **Reutilização**: Herança e composição eficientes
- **Manutenibilidade**: Mudanças localizadas e controláveis
- **Testabilidade**: Classes podem ser testadas isoladamente
- **Escalabilidade**: Fácil extensão e modificação

### **Para o Negócio**

- **Flexibilidade**: Adaptação rápida a novos requisitos
- **Qualidade**: Menor incidência de bugs
- **Produtividade**: Desenvolvimento mais eficiente
- **Evolução**: Facilidade para crescer e adaptar sistemas

## 📊 Comparativo de Paradigmas

| Aspecto | Programação Procedural | Programação Orientada a Objetos |
|---------|------------------------|-----------------------------------|
| **Organização** | Funções isoladas | Classes coesas |
| **Dados** | Variáveis globais | Encapsulados em objetos |
| **Reutilização** | Copy-paste de código | Herança e composição |
| **Manutenção** | Modificações espalhadas | Mudanças localizadas |
| **Complexidade** | Boa para problemas simples | Excelente para sistemas complexos |
| **Modelagem** | Foco em processos | Foco em entidades do domínio |

### 📜 Certificados de Conclusão

- 🏆 **[Introdução a POO com Python](./Cursos/1.Introdução%20a%20POO/README.md)**
- 🏆 **[Conceitos de Herança em Python](./Cursos/2.Conceitos%20de%20Herança/README.md)**
- 🏆 **[Aplicando Encapsulamento em Python](./Cursos/3.Encapsulamento/README.md)**
- 🏆 **[Conhecendo Polimorfismo em Python](./Cursos/4.Polimorfismo/README.md)**
- 🏆 **[Interfaces e Classes Abstratas com Python](./Cursos/5.Interfaces%20e%20Classes%20Abstratas/README.md)**

## Certificado de Conclusão do Módulo 04

![Certificado do módulo](https://github.com/user-attachments/assets/84dbadd3-b53b-4af3-bb42-da97712bc51f)

---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 04 - POO e Boas Práticas  
**👨‍💻 Desenvolvido por:** Ithallo Leandro R. Barbosa  
