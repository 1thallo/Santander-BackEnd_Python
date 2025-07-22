"""
Descrição
Uma loja deseja um sistema que registre os produtos disponíveis em estoque e permita verificar se um produto solicitado está disponível.

Entrada
Lista de produtos em estoque.
Nome do produto solicitado.
Saída
"Produto disponível" se o produto estiver no estoque.
"Produto esgotado" caso contrário.
"""

# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input().strip()

# TODO: Verifique se o produto está no estoque:
if produto in estoque:
    print("Produto disponível")
else:
    print("Produto esgotado")