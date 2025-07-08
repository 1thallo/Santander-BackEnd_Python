# Tuplas são imutáveis, criadas através da classe Tuple
# Built-in immutable sequence.

# * DECLARAÇÃO DE TUPLA

# virgula no final
frutas = ("laranja", "maca", "uva",)

# classe tuple
letras = tuple("python") 

# passando uma lista
numeros = tuple([1, 2, 3, 4])


# * ACESSO AOS ELEMENTOS
frutas[0]  # laranja
frutas[1]  # maca
frutas[-1]  # uva

# * TUPLAS ANINHADAS (MATRIZ)
matriz = ((1, "a", 2), ("b", 3, 4), (6, 5, "c"))

matriz[0] # (1, "a", 2)
matriz[0][0]  # 1
matriz[0][-1] # 2
matriz[-1][-1]  # c

# * FATIAMENTO
tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:]  # "t", "h", "o", "n"
tupla[:2]  # "p", "y"
tupla[1:3]  # "y", "t"