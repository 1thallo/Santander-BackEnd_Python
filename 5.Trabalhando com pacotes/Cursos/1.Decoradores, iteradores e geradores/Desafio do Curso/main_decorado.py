from models_decorado import Banco, GeradorRelatorio, ContaIterador

def demonstrar_decoradores():
    """Demonstra o funcionamento dos decoradores de log"""
    print("\t🎯 DEMONSTRAÇÃO DE DECORADORES")
    print("=" * 50)
    
    # Criar banco
    banco = Banco("Banco Ithallo")
    
    # Criar clientes (com log automático)
    cliente1 = banco.criar_cliente("João Silva", "12345678901")
    cliente2 = banco.criar_cliente("Maria Santos", "98765432100")
    
    print()
    
    # Criar contas (com log automático)
    conta1 = banco.criar_conta(cliente1)
    conta2 = banco.criar_conta(cliente2)
    
    print()
    
    # Realizar transações (com log automático)
    conta1.depositar(1000.0)
    conta1.sacar(250.0)
    conta1.depositar(500.0)
    
    conta2.depositar(750.0)
    conta2.sacar(100.0)
    
    return banco

def demonstrar_gerador_relatorio(banco):
    """Demonstra o gerador de relatórios"""
    print("\n🎯 DEMONSTRAÇÃO DO GERADOR DE RELATÓRIOS")
    print("=" * 50)
    
    conta = banco.contas[0]  # Primeira conta
    gerador = GeradorRelatorio(conta)
    
    print(f"📊 Relatório da Conta {conta.numero} - {conta.cliente.nome}")
    print("-" * 40)
    
    # Gerar todas as transações
    print("\n📋 TODAS AS TRANSAÇÕES:")
    for i, transacao in enumerate(gerador.gerar_todas_transacoes(), 1):
        data_formatada = transacao['data'].strftime("%d/%m/%Y %H:%M:%S")
        print(f"{i}. {transacao['tipo']: <8} | R$ {transacao['valor']:>8.2f} | {data_formatada}")
    
    # Gerar apenas depósitos
    print("\n💰 APENAS DEPÓSITOS:")
    for i, transacao in enumerate(gerador.gerar_por_tipo('Depósito'), 1):
        data_formatada = transacao['data'].strftime("%d/%m/%Y %H:%M:%S")
        print(f"{i}. R$ {transacao['valor']:>8.2f} | {data_formatada}")
    
    # Gerar apenas saques
    print("\n💸 APENAS SAQUES:")
    for i, transacao in enumerate(gerador.gerar_por_tipo('Saque'), 1):
        data_formatada = transacao['data'].strftime("%d/%m/%Y %H:%M:%S")
        print(f"{i}. R$ {transacao['valor']:>8.2f} | {data_formatada}")

def demonstrar_iterador_contas(banco):
    """Demonstra o iterador personalizado de contas"""
    print("\n🎯 DEMONSTRAÇÃO DO ITERADOR DE CONTAS")
    print("=" * 50)
    
    # Criar iterador
    iterador = ContaIterador(banco.contas)
    
    print("🏦 INFORMAÇÕES DAS CONTAS:")
    print("-" * 40)
    
    # Usar o iterador
    for info in iterador:
        print(f"Conta: {info['numero']:>3} | "
              f"Titular: {info['titular']:<15} | "
              f"CPF: {info['cpf']:<11} | "
              f"Saldo: R$ {info['saldo']:>8.2f} | "
              f"Transações: {info['qtd_transacoes']}")

def menu_interativo(banco):
    """Menu interativo para testar as funcionalidades"""
    while True:
        print("\n" + "="*50)
        print("🏦 SISTEMA BANCÁRIO COM DECORADORES")
        print("="*50)
        print("[1] Realizar Depósito")
        print("[2] Realizar Saque")
        print("[3] Ver Relatório de Transações")
        print("[4] Listar Todas as Contas")
        print("[0] Sair")
        
        opcao = input("\n=> ").strip()
        
        if opcao == "1":
            try:
                num_conta = int(input("Número da conta: "))
                valor = float(input("Valor do depósito: R$ "))
                
                if 1 <= num_conta <= len(banco.contas):
                    conta = banco.contas[num_conta - 1]
                    conta.depositar(valor)
                else:
                    print("⚠️ Conta não encontrada!")
            except ValueError:
                print("⚠️ Valor inválido!")
        
        elif opcao == "2":
            try:
                num_conta = int(input("Número da conta: "))
                valor = float(input("Valor do saque: R$ "))
                
                if 1 <= num_conta <= len(banco.contas):
                    conta = banco.contas[num_conta - 1]
                    conta.sacar(valor)
                else:
                    print("⚠️ Conta não encontrada!")
            except ValueError:
                print("⚠️ Valor inválido!")
        
        elif opcao == "3":
            try:
                num_conta = int(input("Número da conta: "))
                
                if 1 <= num_conta <= len(banco.contas):
                    conta = banco.contas[num_conta - 1]
                    gerador = GeradorRelatorio(conta)
                    
                    print(f"\n📊 Relatório da Conta {conta.numero}")
                    print("-" * 30)
                    
                    if not conta.transacoes:
                        print("Nenhuma transação encontrada.")
                    else:
                        for i, transacao in enumerate(gerador.gerar_todas_transacoes(), 1):
                            data = transacao['data'].strftime("%d/%m/%Y %H:%M")
                            print(f"{i}. {transacao['tipo']}: R$ {transacao['valor']:.2f} - {data}")
                else:
                    print("⚠️ Conta não encontrada!")
            except ValueError:
                print("⚠️ Número inválido!")
        
        elif opcao == "4":
            demonstrar_iterador_contas(banco)
        
        elif opcao == "0":
            print("\n👋 Sistema encerrado!")
            break
        
        else:
            print("⚠️ Opção inválida!")

def main():
    """Função principal"""
    print("🚀 INICIANDO DEMONSTRAÇÕES")
    print("="*50)
    
    # 1. Demonstrar decoradores
    banco = demonstrar_decoradores()
    
    # 2. Demonstrar gerador de relatórios
    demonstrar_gerador_relatorio(banco)
    
    # 3. Demonstrar iterador de contas
    demonstrar_iterador_contas(banco)
    
    # 4. Menu interativo
    print("\n🎮 INICIANDO MODO INTERATIVO")
    menu_interativo(banco)

if __name__ == "__main__":
    main()