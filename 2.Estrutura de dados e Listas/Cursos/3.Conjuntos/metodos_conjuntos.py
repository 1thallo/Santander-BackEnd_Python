
# * UNION - União
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))  # {1, 2, 3, 4}

# * INTERSECTION - Presente em ambos os conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

print(conjunto_a.intersection(conjunto_b))  # {3}

# * DIFFERENCE - Diferença entre conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}

# * SYMMETRIC_DIFFERENCE - União das diferenças
print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

# * ISSUBSET - Booleano -> Indica se há sub conjunto
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}

print(conjunto_a.issubset(conjunto_b))  # True - Tudo que está contido em A faz parte de B
print(conjunto_b.issubset(conjunto_a))  # False -  Tudo que está contido em B, não faz parte de A

# * ISSUPERSET - Indica se é conjunto pai de outro
print(conjunto_a.issuperset(conjunto_b))  # False -  Tudo que está contido em B, não faz parte de A
print(conjunto_b.issuperset(conjunto_a))  # True - Tudo que está contido em A faz parte de B

# * ISDISJOINT - Indica se os elementos de um conjunto não estão em outro
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

# * ADD - Adicionar elementos dentro de um conjunto
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
sorteio.add(80) # {1, 23, 25, 80}

#  * CLEAR - Limpar os elementos de um conjunto

# * COPY - Criar uma cópia independente do conjunto principal

# * DISCARD - Descarta um elemento do conjunto (Se o elemento não existe, somente continua, sem erro)
numero = {1, 3, 5, 7, 11, 14}
numero.discard(3)
print(numero) # {1, 5, 7, 11, 14}

# * POP - Tira elementos em ordem do conjunto
numeros = {0,1,2,3,4,5,6,7}

print(numeros.pop())  # 0
print(numeros.pop())  # 1

print(numeros)  # {2, 3, 4, 5, 6, 7}

# * REMOVE - Remove elemento do conjunto por parâmetro (Se o elemento não existe, dá um erro - KeyError)
numeros = {0,1,2,3,4,5,6,7}

numeros.remove(2)

print(numeros) # {0, 1, 3, 4, 5, 6, 7}

# * LEN - Tamanho de elementos do conjunto
numeros = {0,1,2,3,4,5,6,7}
print(len(numeros))  # 7

# * IN - Verificar a existência de um elemento no conjunto
1 in numeros  # True


