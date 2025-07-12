class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = True
        print("zzZZ")
    
    def __del__(self):
        print("Removendo a instância da classe")

def criar_cachorro():
    c = Cachorro("Fred", "branco", False)
    print(c.nome)

criar_cachorro()
