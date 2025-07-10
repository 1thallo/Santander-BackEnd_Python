# Sistema Bancário com Funções - Versão Otimizada
from funcoes_sistema_bancario import *

# Constantes
LIMITE_SAQUE = 3
VALOR_MAX_SAQUE = 500
AGENCIA = "0001"

def main():
    """Função principal do sistema"""
    # Variáveis locais
    saldo = 0
    numero_saques = 0
    extrato = ""
    usuarios = []
    contas = []
    
    menu = """
========== BANCO ITHALLO ==========
    
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[7] Listar usuários
[0] Sair

=> """
    
    while True:
        opcao = input(menu)
        
        match opcao:
            case "1":
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = deposito(saldo, valor, extrato)
                
            case "2":
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato = saque(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUE,
                    limite_valor=VALOR_MAX_SAQUE,
                )
                
            case "3":
                exibir_extrato(saldo, extrato=extrato)
                
            case "4":
                usuarios = criar_usuario(usuarios)
                
            case "5":
                contas = criar_conta(usuarios, contas, AGENCIA)
                
            case "6":
                listar_contas(contas)
                
            case "7":  # Nova opção
                listar_usuarios(usuarios)
                
            case "0":
                print("\nObrigado por usar o Banco Ithallo! Até mais! 🫡")
                break
                
            case _:
                print("⚠️ Operação inválida! Selecione novamente.")

if __name__ == "__main__":
    main()

