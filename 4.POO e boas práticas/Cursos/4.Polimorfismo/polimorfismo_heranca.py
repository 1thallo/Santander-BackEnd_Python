# Mesmo método com comportamento diferente
class Passaro:
    def voar(self):
        pass

class Pardal(Passaro):
    def voar(self):
        print("Pardal voando...")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa.")

def plano_de_voo(objeto):
    objeto.voar()

pardal = Pardal()
avestruz = Avestruz()

plano_de_voo(pardal)
plano_de_voo(avestruz)

