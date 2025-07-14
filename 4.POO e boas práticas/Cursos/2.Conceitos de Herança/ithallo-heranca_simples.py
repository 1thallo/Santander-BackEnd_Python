"""
🚗 EXEMPLO DE HERANÇA SIMPLES

Hierarquia de Classes:

        ┌─────────────┐
        │   Veiculo   │ ← Classe Pai (Superclasse)
        │             │
        │ - marca     │
        │ - modelo    │
        │ - ano       │
        │             │
        │ + ligar()   │
        │ + desligar()│
        └─────────────┘
               │
               │ inherits
               ▼
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│  Moto   │ │  Carro  │ │ Caminhão│ ← Classes Filhas (Subclasses)
│         │ │         │ │         │
│ + empinar│ + abrir_ │ + carregar│
│   ()     │  porta() │   _carga()│
└─────────┘ └─────────┘ └─────────┘

"""

# * Classe Pai (Superclasse)
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"🔑 {self.marca} {self.modelo} ligado!")
        else:
            print("⚠️ Veículo já está ligado!")
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"🔒 {self.marca} {self.modelo} desligado!")
        else:
            print("⚠️ Veículo já está desligado!")
    
    def acelerar(self):
        if self.ligado:
            print(f"🚀 {self.marca} {self.modelo} acelerando...")
        else:
            print("⚠️ Ligue o veículo primeiro!")

# * Classes Filhas (Subclasses)
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)  # chama o construtor da classe pai
        self.cilindradas = cilindradas
    
    def empinar(self):
        if self.ligado:
            print(f"🏍️ {self.marca} {self.modelo} empinando! É os D, vida!❤️")
        else:
            print("⚠️ Ligue a moto primeiro!")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
        self.porta_aberta = False
    
    def abrir_porta(self):
        if not self.porta_aberta:
            self.porta_aberta = True
            print(f"🚗 Porta do {self.marca} {self.modelo} aberta!")
        else:
            print("⚠️ Porta já está aberta!")
    
    def fechar_porta(self):
        if self.porta_aberta:
            self.porta_aberta = False
            print(f"🚗 Porta do {self.marca} {self.modelo} fechada!")
        else:
            print("⚠️ Porta já está fechada!")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.capacidade_carga = capacidade_carga
        self.carga_atual = 0
    
    def carregar_carga(self, peso):
        if self.carga_atual + peso <= self.capacidade_carga:
            self.carga_atual += peso
            print(f"🚛 Carregando {peso}kg no {self.marca} {self.modelo}")
            print(f"📦 Carga atual: {self.carga_atual}kg/{self.capacidade_carga}kg")
        else:
            print(f"⚠️ Excesso de carga! Capacidade máxima: {self.capacidade_carga}kg")
    
    def descarregar(self):
        if self.carga_atual > 0:
            print(f"📤 Descarregando {self.carga_atual}kg do {self.marca} {self.modelo}")
            self.carga_atual = 0
        else:
            print("⚠️ Caminhão já está vazio!")

# * Demonstração da Herança
print("=" * 50)
print("🚗 DEMONSTRAÇÃO DE HERANÇA SIMPLES")
print("=" * 50)

# * instâncias
moto = Motocicleta("Honda", "CB600", 2023, 600)
carro = Carro("Toyota", "Corolla", 2022, 4)
caminhao = Caminhao("Volvo", "FH540", 2021, 15000)

print("\n🏍️ TESTANDO MOTOCICLETA:")
print("-" * 30)
moto.ligar()        # * Método herdado
moto.acelerar()     # * Método herdado
moto.empinar()      # ! Método próprio

print("\n🚗 TESTANDO CARRO:")
print("-" * 30)
carro.ligar()       # * Método herdado
carro.abrir_porta() # ! Método próprio
carro.acelerar()    # * Método herdado
carro.fechar_porta()# ! Método próprio

print("\n🚛 TESTANDO CAMINHÃO:")
print("-" * 30)
caminhao.ligar()           # * Método herdado
caminhao.carregar_carga(5000)  # ! Método próprio
caminhao.carregar_carga(12000) # ! Método próprio
caminhao.acelerar()        # * Método herdado
caminhao.descarregar()     # ! Método próprio

print("\n🔍 VERIFICANDO HERANÇA:")
print("-" * 30)
print(f"Moto é instância de Veiculo? {isinstance(moto, Veiculo)}")
print(f"Carro é instância de Veiculo? {isinstance(carro, Veiculo)}")
print(f"Caminhão é instância de Veiculo? {isinstance(caminhao, Veiculo)}")

print("\n📊 INFORMAÇÕES DOS VEÍCULOS:")
print("-" * 30)
veiculos = [moto, carro, caminhao]

for veiculo in veiculos:
    print(f"🚙 {veiculo.__class__.__name__}: {veiculo.marca} {veiculo.modelo} ({veiculo.ano})")