def decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes da funcao!")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois da funcao!")
        return resultado 
    
    return envelope

@decorador
def boas_vindas(nome):
    print(f"Ola {nome}, seja bem vindo!🫡")
    return nome.upper()

resultado = boas_vindas("Ithallo")
print(resultado)    # ITHALLO

# * Faz algo antes da funcao!
# ! Ola Ithallo, seja bem vindo!🫡
# * Faz algo depois da funcao!
# * ITHALLO

