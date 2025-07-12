
# * CONCEITO - EXEMPLO
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")
    
    def dormir(self):
        self.acordado = True
        print("zzZZ")

cachorro = Cachorro("dog", "caramelo", True)
cachorrito = Cachorro("cachorrito", "marrom", False)

print(cachorrito.acordado)  # False
cachorrito.latir()      # Auau
cachorrito.dormir()     # zzZZ
print(cachorrito.acordado)  # True

