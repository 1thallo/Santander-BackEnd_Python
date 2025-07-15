# * Exemplo
class Conta:
    def __init__(self, nr_agencia, saldo = 0):
        self._saldo = saldo     # inicia com underline, indicando status privado
        self.nr_agencia = nr_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
    
    def mostrar_saldo(self):
        return self._saldo

conta = Conta("001" , 100)
print(conta._saldo)     # ! Ainda possível acessar, porém é uma má prática
print(conta.mostrar_saldo())        # * Forma correta de acessar atributo privado da classe, através de um método