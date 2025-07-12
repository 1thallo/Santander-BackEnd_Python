class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Bip-bip!📯")
    
    def parar(self):
        print("Freando...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummm...")
    
    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join({f"{chave}: {valor}" for chave, valor in self.__dict__.items()})}"

bicicleta_1 = Bicicleta("cinza", "caloi", 2022, 1500)
bicicleta_1.buzinar()  # Bip-bip
bicicleta_1.parar()     #Freando...\n  Bicicleta parada!
bicicleta_1.correr()    # Vrummm...
print(bicicleta_1.cor, bicicleta_1.modelo, bicicleta_1.ano, bicicleta_1.valor)  # cinza caloi 2022 1500
print(bicicleta_1)      # Retorna o método __str__ "Bicicleta: modelo: caloi, ano: 2022, valor: 1500, cor: cinza"
