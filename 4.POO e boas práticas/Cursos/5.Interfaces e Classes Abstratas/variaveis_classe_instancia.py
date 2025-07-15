class Estudante:
    escola = "Catolica"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome}: {self.matricula} ({self.escola})"

estudante1 = Estudante("Ithallo", "UC40028922")
estudante2 = Estudante("Leandro", "UC09707070")
print(estudante1)       # Ithallo: UC40028922 (Catolica)
print(estudante2)       # Leandro: UC09707070 (Catolica)

estudante1.escola = "JMJ"
print(estudante1)       # Ithallo: UC40028922 (JMJ)
print(estudante2)       # Leandro: UC09707070 (Catolica)

Estudante.escola = "Python"

estudante3 = Estudante("Rodrigues", "UC3333333")
print(estudante3)       # Rodrigues: UC3333333 (Python)
