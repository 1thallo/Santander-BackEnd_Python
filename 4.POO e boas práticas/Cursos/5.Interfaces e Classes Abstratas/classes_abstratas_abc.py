from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod     # Com os metódos abstratos, é obrigatório definir os métodos
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):    #Obrigatório
        print("Ligando a TV...\nLigado!")
    
    def desligar(self): #Obrigatório
        print("Desligando a TV...\nDesligado!")

class ControleAC(ControleRemoto):
    def ligar(self):    #Obrigatório
        print("Ligando o Ar Condiconado...")
        print("Ligado!")
    
    def desligar(self): #Obrigatório
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

controle = ControleTV()
controle.ligar()
controle.desligar()

controleAC = ControleAC()
controleAC.ligar()
controleAC.desligar()
