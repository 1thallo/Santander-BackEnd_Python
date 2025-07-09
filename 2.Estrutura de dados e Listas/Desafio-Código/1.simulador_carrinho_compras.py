"""
🛒 SIMULADOR DE CARRINHO DE COMPRAS

📋 Descrição:
Crie um sistema de carrinho de compras que permita adicionar produtos 
e calcular o valor total da compra.

📥 Entrada:
- Número de produtos a serem adicionados
- Lista de produtos (cada linha contém nome e preço separados por espaço)

📤 Saída:
- Lista dos produtos adicionados com seus respectivos preços
- Valor total da compra

📝 Exemplo:
Entrada:
2
Pão 3.50
Leite 4.00

Saída:
Pão: R$3.50
Leite: R$4.00
Total: R$7.50
"""

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# TODO: Exiba os itens e o total da compra - Resposta
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

print(f"Total: R${total:.2f}")