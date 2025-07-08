# Exemplo
frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

# * ACESSO DIRETO DE LISTA
frutas = ["maçã", "laranja", "uva", "pera"]
frutas[0] # maçã
frutas[1] # laranja

# * INDICE NEGATIVO
frutas[-1] # pera
frutas[-3] # laranja

# * LISTA ANINHADA (MATRIZ)
matriz = [[1, "a", 2], ["b", 3, 4], [6, 5, "c"]]

matriz[0]  # [1, "a", 2]
matriz[0][0]  # 1
matriz[0][-1]  # 2
matriz[-1][-1]  # "c"

# * FATIAMENTO
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ['n', 'o', 'h', 't', 'y', 'p']

# * ITERAR LISTA
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro, end=" ") # gol celta palio

# * COMPREENSÃO DE LISTA
numeros = [1, 30, 21, 2, 9, 65, 34]

pares = [numero_par for numero_par in numeros if numero_par % 2 == 0]
quadrado = [num_quadrado**2 for num_quadrado in numeros]
