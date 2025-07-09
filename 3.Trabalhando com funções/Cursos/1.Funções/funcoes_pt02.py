
# * PARÂMETROS ESPECIAIS
# Restrição de argumentos

"""
def funcao(pos1, pos2, /, pos or keyword, *, keyword1, keyword2):
            _________     _______________    __________________  
                |               |                     |
    Apenas Posicional     Posicional ou       Apenas Palavra-Chave
                            Palavra-Chave
"""

# -> Tudo antes da ("/") é parâmetro por posição, tudo depois do ("*") é parâmetro por palavra

# * APENAS POSICONAL
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):  # * Modelo, ano e placa são passados APENAS por posição. Marca, motor e combustível devem ser passados por posição ou palavra-chave
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina")    # * VÁLIDO

criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina")    # ! INVÁLIDO: criar_carro() got some positional-only arguments passed as keyword arguments: 'modelo, ano, placa'

# * APENAS PALAVRA-CHAVE
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):  # * Todos os parâmetros devem ser por palavra-chave, depois do ("*")
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina")    # * VÁLIDO

criar_carro("Palio", 1999, "ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina")    # ! INVÁLIDO

# * POSIÇÃO E PALAVRA-CHAVE
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):  # * Modelo, ano e placa são passados APENAS por posição. Marca, motor e combustível devem ser passados APENAS POR palavra-chave
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina")    # * VÁLIDO
criar_carro(modelo="Palio", ano=1999, placa="ABC-123", marca="Fiat", motor="1.0", combustivel="Gasolina")    # ! INVÁLIDO

# -----------------------------------------------------------------------------------------------------
# * OBJETOS DE PRIMEIRA CLASSE - Função como parâmetro
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def resultado_soma(x, y, funcao_soma):
    resultado = funcao_soma(x, y)
    print(f"O resultado da operação é igual a {resultado}")

resultado_soma(10, 10, somar)       # O resultado da operação é igual a 20
resultado_soma(10, 10, subtrair)       # O resultado da operação é igual a 0

# -----------------------------------------------------------------------------------------------------
# * ESCOPO LOCAL E GLOBAL
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return

print(salario_bonus(500))  # 2500