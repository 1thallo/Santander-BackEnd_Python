from models import PessoaFisica, ContaCorrente, Deposito, Saque
from utils import (
    filtrar_cliente, 
    recuperar_conta_cliente, 
    obter_dados_cliente,
    obter_valor_operacao,
    listar_contas_formatadas,
    listar_clientes_formatados,
    exibir_extrato_formatado,
    validar_cpf
)


def menu():
    """Exibe o menu principal do sistema"""
    return """
╔══════════════════════════════════════╗
║         BANCO ITHALLO - OOP          ║
╠══════════════════════════════════════╣
║  [1] Depositar                       ║
║  [2] Sacar                           ║
║  [3] Extrato                         ║
║  [4] Novo cliente                    ║
║  [5] Nova conta                      ║
║  [6] Listar contas                   ║
║  [7] Listar clientes                 ║
║  [0] Sair                            ║
╚══════════════════════════════════════╝

=> """


def depositar(clientes):
    """Operação de depósito"""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n⚠️ Cliente não encontrado!")
        return
    
    valor = obter_valor_operacao("depósito")
    transacao = Deposito(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    """Operação de saque"""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n⚠️ Cliente não encontrado!")
        return
    
    valor = obter_valor_operacao("saque")
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    """Exibe extrato da conta"""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n⚠️ Cliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    exibir_extrato_formatado(conta)


def criar_cliente(clientes):
    """Cria um novo cliente"""
    dados = obter_dados_cliente()
    
    # Verifica se CPF já existe
    if filtrar_cliente(dados["cpf"], clientes):
        print("\n⚠️ Já existe cliente com esse CPF!")
        return
    
    cliente = PessoaFisica(
        nome=dados["nome"],
        data_nascimento=dados["data_nascimento"],
        cpf=dados["cpf"],
        endereco=dados["endereco"]
    )
    
    clientes.append(cliente)
    print("\n✅ Cliente criado com sucesso!")


def criar_conta(numero_conta, clientes, contas):
    """Cria uma nova conta para um cliente"""
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n⚠️ Cliente não encontrado!")
        print("💡 Cadastre o cliente primeiro na opção [4]")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\n✅ Conta criada com sucesso!")
    print(f"📄 Agência: {conta.agencia}")
    print(f"📄 Número: {conta.numero}")
    print(f"👤 Titular: {conta.cliente.nome}")


def listar_contas(contas):
    """Lista todas as contas"""
    listar_contas_formatadas(contas)


def listar_clientes(clientes):
    """Lista todos os clientes"""
    listar_clientes_formatados(clientes)


def main():
    """Função principal do sistema"""
    clientes = []
    contas = []
    
    print("🏦 Bem-vindo ao Sistema Bancário OOP!")
    
    while True:
        try:
            opcao = input(menu()).strip()
            
            match opcao:
                case "1":
                    depositar(clientes)
                
                case "2":
                    sacar(clientes)
                
                case "3":
                    exibir_extrato(clientes)
                
                case "4":
                    criar_cliente(clientes)
                
                case "5":
                    numero_conta = len(contas) + 1
                    criar_conta(numero_conta, clientes, contas)
                
                case "6":
                    listar_contas(contas)
                
                case "7":
                    listar_clientes(clientes)
                
                case "0":
                    print("\n👋 Obrigado por usar o Banco Ithallo!")
                    print("🫡 Sistema encerrado com sucesso!")
                    break
                
                case _:
                    print("\n⚠️ Operação inválida! Tente novamente.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Sistema interrompido pelo usuário!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("🔄 Tente novamente ou reinicie o sistema.")


if __name__ == "__main__":
    main()