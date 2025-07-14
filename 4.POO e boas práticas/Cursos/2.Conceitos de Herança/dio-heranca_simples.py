class Veiculo():
    def __init__(self, cor, placa, numero_rodas, ):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor...")

    def acelerar(self):
        print("Acelerando...")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"
        
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Nao"} estou carregado!")
    
    

moto = Motocicleta("azul", "0110ITH", 2)
carro = Carro("preto", "4002ITH", 4)
caminhao = Caminhao("azul", "CAM110H", 6, False)

moto.ligar_motor()
carro.ligar_motor()
caminhao.ligar_motor()
caminhao.esta_carregado()
print(moto)
print(carro)
print(caminhao)
