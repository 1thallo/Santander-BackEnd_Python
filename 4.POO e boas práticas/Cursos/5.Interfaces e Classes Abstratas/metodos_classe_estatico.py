class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_da_dt_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def is_maior_idade(idade):
        return idade >= 18
            

# p1 = Pessoa("Ithallo", 20)
# print(p1.nome, p1.idade)

p = Pessoa.criar_da_dt_nascimento(2004, 10, 1, "Ithallo")
print(p.nome, p.idade)      #  Ithallo 21

print(Pessoa.is_maior_idade(18))        # True
print(Pessoa.is_maior_idade(16))        # False