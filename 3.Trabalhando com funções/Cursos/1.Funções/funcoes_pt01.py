
# * DECLARAÇÃO
def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo {nome}!")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Seja bem-vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2("Ithallo")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Leandro")

# -----------------------------------------------
# * RETURN
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_total([10, 20, 30]))     # 60
print(retorna_antecessor_e_sucessor(10))    # (9, 11)

# -----------------------------------------------
# * ARGUMENTOS NOMEADOS
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-123")    # * -> Desvantagem, em relação a ordenação obrigatória

salvar_carro(marca = "Fiat", modelo="Palio", ano=1999, placa="ABC-123")     # * -> Argumento nomeado evita erros de sequências e ordenação

salvar_carro(**{'marca':'Fiat', 'modelo':'Palio', 'ano':1999, 'placa': 'ABC-123'})      # * -> Recebe um dicionário

# -----------------------------------------------
# * *ARGS e **KWARGS (tuplas, dicionários)
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Quarta-feira, 01 de outubro de 2004","Zen of Python", "Beautiful is better than ugly", autor = "Tim Peters", ano = 1999)