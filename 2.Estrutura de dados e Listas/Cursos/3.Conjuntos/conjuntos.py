# Não permitem duplicação

# * DECLARAÇÃO
print(set([1, 2, 3, 1, 3, 4]))  # {1, 2, 3, 4 }

print(set("abacaxi"))  # {'i', 'a', 'c', 'b', 'x'}

print(set(("palio", "gol", "celta", "palio")))  # {'celta', 'gol', 'palio'}

# * ACESSO AOS DADOS - Necessário converter para lista
numeros = {1, 2, 3, 4}

numeros = list(numeros)
print(numeros)  # [1, 2, 3, 4]
print(numeros[0]) # 1
