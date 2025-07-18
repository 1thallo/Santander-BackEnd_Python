from abc import ABC, abstractmethod
from datetime import datetime
import functools
import os

# Decorador de Log para Arquivo
def log_transacao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Executar a função
        resultado = func(*args, **kwargs)
        
        # Preparar informações do log
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        nome_funcao = func.__name__
        
        argumentos = []
        if args:
            for i, arg in enumerate(args[1:], 1):
                if isinstance(arg, (int, float, str)):
                    argumentos.append(f"arg{i}={arg}")
                else:
                    argumentos.append(f"arg{i}={type(arg).__name__}")
        
        if kwargs:
            for key, value in kwargs.items():
                argumentos.append(f"{key}={value}")
        
        args_str = ", ".join(argumentos) if argumentos else "sem argumentos"
        
        valor_retornado = str(resultado) if resultado is not None else "None"
        
        linha_log = f"[{data_hora}] Função: {nome_funcao} | Argumentos: {args_str} | Retorno: {valor_retornado}\n"
        
        script_dir = os.path.dirname(__file__)
        arquivo_log = os.path.join(script_dir, "log.txt")
        
        with open(arquivo_log, "a", encoding="utf-8") as file:
            file.write(linha_log)
        
        print(f"[LOG] {data_hora} - Ação: {nome_funcao.replace('_', ' ').title()}")
        
        return resultado
    return wrapper

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ('{self.cpf}')"
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._transacoes = []
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ('{self._numero}')"
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def transacoes(self):
        return self._transacoes
    
    @log_transacao
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            transacao = {
                'tipo': 'Depósito',
                'valor': valor,
                'data': datetime.now(),
                'saldo_anterior': self._saldo - valor,
                'saldo_atual': self._saldo
            }
            self._transacoes.append(transacao)
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("⚠️ Valor inválido para depósito!")
            return False
    
    @log_transacao
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            transacao = {
                'tipo': 'Saque',
                'valor': valor,
                'data': datetime.now(),
                'saldo_anterior': self._saldo + valor,
                'saldo_atual': self._saldo
            }
            self._transacoes.append(transacao)
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("⚠️ Saldo insuficiente ou valor inválido!")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ('{self._numero}')"
    
    @log_transacao
    def sacar(self, valor):
        numero_saques = len([
            transacao for transacao in self.transacoes
            if transacao['tipo'] == 'Saque'
        ])
        
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques
        
        if excedeu_limite:
            print("\n⚠️ Operação falhou! O valor do saque excede o limite.")
            return False
        elif excedeu_saques:
            print("\n⚠️ Operação falhou! Número máximo de saques excedido.")
            return False
        else:
            return super().sacar(valor)

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        self.clientes = []
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ('{self.nome}')"
    
    @log_transacao
    def criar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"✅ Cliente {nome} criado com sucesso!")
        return cliente
    
    @log_transacao
    def criar_conta(self, cliente, tipo_conta="corrente"):
        numero = len(self.contas) + 1
        
        if tipo_conta == "corrente":
            conta = ContaCorrente(numero, cliente)
        else:
            conta = Conta(numero, cliente)
            
        self.contas.append(conta)
        cliente.adicionar_conta(conta)
        print(f"✅ Conta {numero} criada para {cliente.nome}!")
        return conta

# Gerador de Relatórios
class GeradorRelatorio:
    def __init__(self, conta):
        self.conta = conta
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ('{self.conta.numero}')"
    
    def gerar_todas_transacoes(self):
        """Gerador que retorna todas as transações uma por vez"""
        for transacao in self.conta.transacoes:
            yield transacao
    
    def gerar_por_tipo(self, tipo_filtro):
        """Gerador que filtra transações por tipo"""
        for transacao in self.conta.transacoes:
            if transacao['tipo'].lower() == tipo_filtro.lower():
                yield transacao

# Iterador Personalizado
class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self.indice = 0
    
    def __repr__(self):
        return f"{self.__class__.__name__}: ({len(self.contas)} contas)"
    
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

# Classe para gerenciar logs
class GerenciadorLog:
    @staticmethod
    def ler_log():
        """Lê e exibe o conteúdo do arquivo de log"""
        script_dir = os.path.dirname(__file__)
        arquivo_log = os.path.join(script_dir, "log.txt")
        
        if os.path.exists(arquivo_log):
            print("\n🔍 CONTEÚDO DO ARQUIVO DE LOG:")
            print("=" * 80)
            
            with open(arquivo_log, "r", encoding="utf-8") as file:
                conteudo = file.read()
                if conteudo.strip():
                    print(conteudo)
                else:
                    print("Arquivo de log está vazio.")
            
            print("=" * 80)
        else:
            print("⚠️ Arquivo de log não encontrado.")
    
    @staticmethod
    def limpar_log():
        """Limpa o arquivo de log"""
        script_dir = os.path.dirname(__file__)
        arquivo_log = os.path.join(script_dir, "log.txt")
        
        with open(arquivo_log, "w", encoding="utf-8") as file:
            file.write("")
        
        print("✅ Arquivo de log limpo!")