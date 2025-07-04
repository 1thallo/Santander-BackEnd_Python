# Sacar, Depositar e Visualizar Extrato

# 3 saques diários com limte maximo de R$ 500
LIMITE_SAQUE = 3
VALOR_MAX_SAQUE = 500

saldo = 0
numero_saques = 0
extrato = ''

while True:
    opcao = input("""-------- BANCO ITHALLO --------\n
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair

Digite sua opção: """)
    
    match opcao:
        case "1":
            valor_deposito = float(input("Insira o valor do depósito: "))
            if 0 < valor_deposito < VALOR_MAX_SAQUE:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print(f"\nDepósito realizado ✅! \nSaldo atual: R$ {saldo:.2f}\n")
            else:
                print("\n⚠️  AVISO:Valor de depósito inválido!")

        case "2":
            if numero_saques >= LIMITE_SAQUE:
                print("\n⚠️  AVISO: Limite de saques diários foi atingido!")
            else:
                valor_saque = float(input("Valor do saque: R$ "))
                if valor_saque <= saldo and valor_saque <= VALOR_MAX_SAQUE and valor_saque > 0:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    print(f"\nSaque realizado com sucesso ✅! \nSaldo atual: R$ {saldo:.2f}\n")
                else:
                    print("\n  ⚠️ AVISO:Operação inválida!")

        case "3":
            print(f"\n-------- 📃EXTRATO --------")
            print(f"{extrato or "Nenhuma movimentação na conta."}")
            print(f"Saldo da conta: R$ {saldo:.2f}\n")

        case "4":
            print()
            print("Obrigado por contar com o banco Ithallo! Até mais. 🫡")
            break
        
        case default:
            print("⚠️   AVISO: Opção inserida inválida!")
        
