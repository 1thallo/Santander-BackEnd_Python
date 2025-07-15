import functools

def decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes da funcao!")
        funcao(*args, **kwargs)
        print("Faz algo depois da funcao!")
    
    return envelope

@decorador
def boas_vindas(nome):
    print(f"Ola {nome}, seja bem vindo!🫡")

print(boas_vindas.__name__)     # boas_vindas