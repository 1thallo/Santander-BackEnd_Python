def decorador(funcao):
    def envelope():
        print("Faz algo antes da função")
        funcao()
        print("Faz algo depois da função")
    return envelope

@decorador
def ola_mundo():
    print("Ola mundo!")

ola_mundo()

"""
Faz algo antes da função
Ola mundo!
Faz algo depois da função
"""