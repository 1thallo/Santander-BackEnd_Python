"""Descrição
Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).

Entrada
Marca, modelo e ano do veículo.

Saída
"Veículo antigo" se o carro tiver mais de 20 anos.
"Veículo novo" caso contrário.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
Toyota
Corolla
2000

Saída
Veículo antigo

Honda
Civic
2005

Saída
Veículo novo

Ford
Fiesta
1999

Saída
Veículo antigo
"""
from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
    def verificar_antiguidade(self):
        if datetime.now().year - self.ano <= 20:
            return "Veículo novo"
        else:
            return "Veículo antigo"

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())