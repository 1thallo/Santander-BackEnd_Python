LIMITE_SAQUE = 3
VALOR_MAX_SAQUE = 500 

#  * Todas as funções do sistema bancário

def saque(*, saldo, extrato, valor, numero_saques, limite_saques=LIMITE_SAQUE, limite_valor=VALOR_MAX_SAQUE):
    if numero_saques >= limite_saques:
        print("ERRO: Número máximo de saques excedido.")
        return saldo, extrato
    
    if valor > limite_valor:
        print("ERRO: O valor do saque excede o limite.")
        return saldo, extrato
    
    if valor > saldo:
        print("ERRO: Saldo insuficiente.")
        return saldo, extrato
    
    if valor <= 0:
        print("ERRO: Valor inválido.")
        return saldo, extrato
    
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor <= 0:
        print("ERRO: Valor inválido.")
        return saldo, extrato
    
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f"\n-------- 📃 EXTRATO --------")
    print(f"{extrato or 'Nenhuma movimentação na conta.'}")
    print(f"Saldo da conta: R$ {saldo:.2f}\n")

def criar_usuario(usuarios):
    """Cadastra um novo usuário no sistema"""
    cpf = input("Digite o CPF (somente números): ")
    
    usuario_existente = filtrar_usuario(cpf, usuarios)
    if usuario_existente:
        print("\n⚠️ Já existe usuário com esse CPF!")
        return usuarios
    
    nome = input("Digite o nome completo: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço completo (logradouro, nº, bairro, cidade/sigla do estado): ")
    
    usuarios.append({ "nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("✅ Usuário criado com sucesso!")
    return usuarios

def filtrar_usuario(cpf, usuarios):
    """Filtra usuário pelo CPF"""
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(usuarios, contas, AGENCIA):
    """Cria uma nova conta bancária"""
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario }
        contas.append(conta)
        print(f"✅ Conta criada com sucesso!")
        print(f"Agência: {AGENCIA}")
        print(f"Conta: {numero_conta}")
        print(f"Titular: {usuario['nome']}")
    else:
        print("\n⚠️ Usuário não encontrado! Cadastre o usuário primeiro.")
    return contas

def listar_contas(contas):
    """Lista todas as contas cadastradas"""
    if not contas:
        print("\n⚠️ Nenhuma conta cadastrada.")
        return
    
    print("\n========== CONTAS CADASTRADAS ==========")
    for conta in contas:
        linha = f"""\
Agência:\t{conta['agencia']}
C/C:\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""

        print(linha)

def listar_usuarios(usuarios):
    """Lista todos os usuários cadastrados"""
    if not usuarios:
        print("\n⚠️ Nenhum usuário cadastrado.")
        return
    
    print("\n========== USUÁRIOS CADASTRADOS ==========")
    for usuario in usuarios:
        linha = f"""\
Nome:\t\t{usuario['nome']}
CPF:\t\t{usuario['cpf']}
Data Nasc.:\t{usuario['data_nascimento']}
Endereço:\t{usuario['endereco']}
"""
        print(linha)