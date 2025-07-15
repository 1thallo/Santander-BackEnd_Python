def gerador(numeros: list[int]):
    for num in numeros:
        yield num * 2

numeros = [1, 3, 5 , 7]
for i in gerador(numeros):
    print(i)