class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"

class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico
    pass

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo
    pass

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Ave, Mamifero):
    pass

gato = Gato(num_patas = 4, cor_pelo="laranja")
print(gato)

ornitorrinco = Ornitorrinco(num_patas = 4, cor_pelo = "marrom", cor_bico="marrom-claro")
print(ornitorrinco)
