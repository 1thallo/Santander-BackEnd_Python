from datetime import datetime

class ContaComLimite:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.transacoes = []  # lista para armazenar transações
        self.limite_diario = 10  # maximo 10 transações por dia
    
    def _contar_transacoes_hoje(self):
        """Conta quantas transações foram feitas hoje"""
        hoje = datetime.now().date()
        transacoes_hoje = 0
        
        for transacao in self.transacoes:
            if transacao['data'].date() == hoje:
                transacoes_hoje += 1
        
        return transacoes_hoje
    
    def _registrar_transacao(self, tipo, valor):
        """Registra a transação na lista"""
        transacao = {
            'tipo': tipo,
            'valor': valor,
            'data': datetime.now(),
            'saldo_anterior': self.saldo - valor if tipo == 'Depósito' else self.saldo + valor,
            'saldo_atual': self.saldo
        }
        self.transacoes.append(transacao)
    
    def depositar(self, valor):
        """Realiza depósito com verificação de limite"""
        
        if self._contar_transacoes_hoje() >= self.limite_diario:
            print("⚠️ LIMITE ATINGIDO: Você já realizou 10 transações hoje!")
            return False
        
        if valor > 0:
            self.saldo += valor
            self._registrar_transacao('Depósito', valor)
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("⚠️ Valor inválido para depósito!")
            return False
    
    def sacar(self, valor):
        """Realiza saque com verificação de limite"""
        
        if self._contar_transacoes_hoje() >= self.limite_diario:
            print("⚠️ LIMITE ATINGIDO: Você já realizou 10 transações hoje!")
            return False
        
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self._registrar_transacao('Saque', valor)
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("⚠️ Saldo insuficiente ou valor inválido!")
            return False
    
    def extrato(self):
        """Mostra extrato com data e hora das transações"""
        print("\n" + "="*50)
        print(f"        EXTRATO - {self.titular}")
        print("="*50)
        
        if not self.transacoes:
            print("Nenhuma transação realizada.")
        else:
            for i, transacao in enumerate(self.transacoes, 1):
                data_formatada = transacao['data'].strftime("%d/%m/%Y %H:%M:%S")
                tipo = transacao['tipo']
                valor = transacao['valor']
                print(f"{i:2d}. {data_formatada} | {tipo:<8} | R$ {valor:>8.2f}")
        
        print("-" * 50)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"Transações hoje: {self._contar_transacoes_hoje()}/{self.limite_diario}")
        print("="*50)

def main():
    """Função principal para testar o sistema"""
    print("🏦 SISTEMA BANCÁRIO COM LIMITE DIÁRIO")
    print("="*50)
    
    conta = ContaComLimite("Ithallo Leandro", 1000.0)
    
    while True:
        print("\n[1] Depositar")
        print("[2] Sacar") 
        print("[3] Extrato")
        print("[4] Testar Limite (fazer 10 transações)")
        print("[0] Sair")
        
        opcao = input("\n=> ").strip()
        
        if opcao == "1":
            try:
                valor = float(input("Valor do depósito: R$ "))
                conta.depositar(valor)
            except ValueError:
                print("⚠️ Valor inválido!")
        
        elif opcao == "2":
            try:
                valor = float(input("Valor do saque: R$ "))
                conta.sacar(valor)
            except ValueError:
                print("⚠️ Valor inválido!")
        
        elif opcao == "3":
            conta.extrato()
        
        elif opcao == "4":
            print("\n🧪 TESTANDO LIMITE DE 10 TRANSAÇÕES...")
            for i in range(12):  # Tentar fazer 12 transações
                print(f"\nTransação {i+1}:")
                if i % 2 == 0:
                    conta.depositar(50.0)
                else:
                    conta.sacar(25.0)
        
        elif opcao == "0":
            print("\n👋 Sistema encerrado!")
            break
        
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    main()