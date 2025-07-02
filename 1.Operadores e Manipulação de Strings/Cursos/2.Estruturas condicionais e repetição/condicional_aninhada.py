conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

## IF ANINHADO
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não possível realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Tipo de conta não reconhecida!")