# METÓDOS DE LISTAS
# * .APPEND()
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, 'Python', [40, 30, 20]]

# * .CLEAR()
lista.clear()
print(lista)    # [] -> limpa a lista

# * .COPY()
lista.copy()
print(lista)  # Cria uma cópia da lista com IDs diferentes, caso delete uma, a cópia permanece

# * .COUNT()
cores = ["vermelho", "azul", "verde", "azul"]
cores.count("vermelho")  # 1
cores.count("azul")  # 2
cores.count("verde") # 1

# * .EXTEND()
linguagens = ["python", "js", "c"]

print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "php"])
print(linguagens)  # ["python", "js", "c", "java", "php"]

# * .INDEX()
print(linguagens.index("java")) # 3
print(linguagens.index("python")) # 0

# * .POP()
linguagens.pop()  # php
linguagens.pop(0)  # * python  -> recebe o indice

# * .REMOVE()
linguagens.remove("c")  # * -> recebe o objeto

# * .REVERSE()
print(linguagens.reverse())

# * .SORT()
linguagens = ["python", "js", "c", "java", "php"]
linguagens.sort()  # ordem alfabética ["c", "csharp", "java", "js", "php", "python"]
linguagens.sort(reverse=True)  # ordem decrescente
linguagens.sort(key=lambda x: len(x))   # por tamanho com lambda
linguagens.sort(key=lambda x: len(x), reverse=True)  #decrescente
