from abc import ABC, abstractmethod
from datetime import datetime
import functools

# Decorador de Log
def log_transacao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # args[0] é sempre 'self' em métodos de instância
        resultado = func(*args, **kwargs)
        
        # Determina o tipo de transação baseado no nome da função
        tipo_transacao = func.__name__.replace('_', ' ').title()
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        print(f"[LOG] {data_hora} - Ação: {tipo_transacao} ")
        
        return resultado
    return wrapper

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._transacoes = []  # Lista para armazenar transações
    
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

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        self.clientes = []
    
    @log_transacao
    def criar_cliente(self, nome, cpf):
        cliente = Cliente(nome, cpf)
        self.clientes.append(cliente)
        print(f"✅ Cliente {nome} criado com sucesso!")
        return cliente
    
    @log_transacao
    def criar_conta(self, cliente):
        numero = len(self.contas) + 1
        conta = Conta(numero, cliente)
        self.contas.append(conta)
        cliente.adicionar_conta(conta)
        print(f"✅ Conta {numero} criada para {cliente.nome}!")
        return conta

# Gerador de Relatórios
class GeradorRelatorio:
    def __init__(self, conta):
        self.conta = conta
    
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