
# * DECLARAÇÃO
pessoa = {"nome": "Ithallo", "idade": 20}
    #ou
pessoa = dict(nome="Ithallo", idade = 20)  # Usando a classe DICT

# * Adicionando uma chave e valor num dicionário já criado
pessoa["telefone"] = 40028922

print(pessoa)   # {'nome': 'Ithallo', 'idade': 20, 'telefone': 40028922}

# * ACESSO AOS DADOS
dados = {'nome': 'Ithallo', 'idade': 20, 'telefone': 40028922}

print(dados["nome"])   # "Ithallo"
print(dados["idade"])  # 20
print(dados["telefone"])   # 40028922

# * Sobrescrevendo valores
dados["nome"] = "Ludimilla"
dados["idade"] = 21
dados["telefone"] = 12341234

print(dados)    # {'nome': 'Ludimilla', 'idade': 21, 'telefone': 12341234}

# * DICIONÁRIOS ANINHADOS
contatos = { 
            "ithallo@gmail.com": {"nome": "Ithallo", "idade": 20, "telefone": 40028922},
            "leandro@gmail.com": {"nome": "Leandro", "idade": 20, "telefone": 12341234},
            "rodrigues@gmail.com": {"nome": "Rodrigues", "idade": 21, "telefone":1357911}
            }

print(contatos["ithallo@gmail.com"]["telefone"])    # 40028922

# * ITERAÇÃO
for chave, valor in contatos.items():
    print(chave, valor)