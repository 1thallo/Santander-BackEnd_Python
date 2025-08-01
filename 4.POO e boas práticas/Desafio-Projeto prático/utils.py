import re
from models import PessoaFisica, ContaCorrente


def validar_cpf(cpf):
    """Valida formato básico do CPF"""
    # Remove caracteres não numéricos
    cpf_numeros = re.sub(r'\D', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf_numeros) != 11:
        return False
    
    # Verifica se não são todos números iguais
    if cpf_numeros == cpf_numeros[0] * 11:
        return False
    
    return True


def formatar_cpf(cpf):
    """Formata CPF para exibição"""
    cpf_limpo = re.sub(r'\D', '', cpf)
    if len(cpf_limpo) == 11:
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    return cpf


def filtrar_cliente(cpf, clientes):
    """Filtra cliente pelo CPF"""
    cpf_limpo = re.sub(r'\D', '', cpf)
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf_limpo]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    """Recupera a conta do cliente (primeira conta)"""
    if not cliente.contas:
        print("\n⚠️ Cliente não possui conta!")
        return None
    
    # Retorna a primeira conta do cliente (pode ser expandido para escolher)
    return cliente.contas[0]


def obter_dados_cliente():
    """Coleta dados do cliente via input"""
    nome = input("Informe o nome completo: ").strip()
    
    while True:
        cpf = input("Informe o CPF (somente números): ").strip()
        if validar_cpf(cpf):
            cpf = re.sub(r'\D', '', cpf)  # Remove formatação
            break
        else:
            print("⚠️ CPF inválido! Digite novamente.")
    
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço completo: ").strip()
    
    return {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }


def obter_valor_operacao(operacao):
    """Obtém valor para operações financeiras"""
    while True:
        try:
            valor = float(input(f"Informe o valor do {operacao}: R$ "))
            if valor <= 0:
                print("⚠️ O valor deve ser positivo!")
                continue
            return valor
        except ValueError:
            print("⚠️ Valor inválido! Digite um número.")


def listar_contas_formatadas(contas):
    """Lista contas com formatação"""
    if not contas:
        print("\n⚠️ Nenhuma conta cadastrada.")
        return
    
    print("\n" + "=" * 50)
    print("           CONTAS CADASTRADAS")
    print("=" * 50)
    
    for conta in contas:
        print(f"""
Agência: {conta.agencia}
Conta: {conta.numero}
Titular: {conta.cliente.nome}
CPF: {formatar_cpf(conta.cliente.cpf)}
Saldo: R$ {conta.saldo:.2f}
{"-" * 30}""")


def listar_clientes_formatados(clientes):
    """Lista clientes com formatação"""
    if not clientes:
        print("\n⚠️ Nenhum cliente cadastrado.")
        return
    
    print("\n" + "=" * 60)
    print("              CLIENTES CADASTRADOS")
    print("=" * 60)
    
    for cliente in clientes:
        print(f"""
Nome: {cliente.nome}
CPF: {formatar_cpf(cliente.cpf)}
Data Nascimento: {cliente.data_nascimento}
Endereço: {cliente.endereco}
Qtd. Contas: {len(cliente.contas)}
{"-" * 40}""")


def exibir_extrato_formatado(conta):
    """Exibe extrato da conta formatado"""
    print("\n" + "=" * 50)
    print("                 EXTRATO")
    print("=" * 50)
    print(f"Agência: {conta.agencia}")
    print(f"Conta: {conta.numero}")
    print(f"Titular: {conta.cliente.nome}")
    print("-" * 50)
    
    transacoes = conta.historico.transacoes
    
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            tipo = transacao['tipo']
            valor = transacao['valor']
            data = transacao['data']
            print(f"{data} | {tipo}: R$ {valor:.2f}")
    
    print("-" * 50)
    print(f"Saldo atual: R$ {conta.saldo:.2f}")
    print("=" * 50)