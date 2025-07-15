def decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes da funcao!")
        funcao(*args, **kwargs)
        print("Faz algo depois da funcao!")
    
    return envelope

@decorador
def boas_vindas(nome):
    print(f"Ola {nome}, seja bem vindo!🫡")

boas_vindas("Ithallo")

# * Faz algo antes da funcao!
# ! Ola Ithallo, seja bem vindo!🫡
# * Faz algo depois da funcao!

