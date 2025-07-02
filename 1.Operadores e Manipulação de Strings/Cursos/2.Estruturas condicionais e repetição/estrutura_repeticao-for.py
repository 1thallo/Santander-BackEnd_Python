texto = 'ithallo' # input("Insira um texto: ")
VOGAIS = "AEIOU"

# Usando iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print()
    print("Executa no final do laço")

## USO DO BUILT-IN RANGE
for i in range (11):
    print(i, end=' ')
else:
    print()

for numero in range (0, 51, 5):   # Tabuada do 5
    print(numero, end=' ')