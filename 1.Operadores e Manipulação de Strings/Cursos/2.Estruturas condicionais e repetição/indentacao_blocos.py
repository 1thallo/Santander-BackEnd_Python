def sacar (valor):
    saldo = 500
    
    if saldo >= valor:
        saldo -= valor
        print('Valor sacado!')
        print(f'Valor atual: {saldo}')
    
    print("Obrigado por ser nosso cliente!")

def depositar(valor):
saldo = 500         # Bloco recuado esperado
saldo += valor 

sacar(100)

