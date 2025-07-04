# Descrição: Uma loja online deseja aplicar descontos em seus produtos com base em cupons de desconto digitados pelos clientes.
# 
# Regras de desconto:
# "DESCONTO10": 10% de desconto.
# "DESCONTO20": 20% de desconto.
# "SEM_DESCONTO": Sem desconto.

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido
if cupom in descontos:
    preco -= preco * descontos[cupom]

print(f"{preco:.2f}")
