
# FROMKEYS - Cria chaves no dicionário
dict.fromkeys(["nome"], ["telefone"])   # {"nome" : None, "telefone": None}

print(dict.fromkeys(["nome", "telefone"], "vazio"))  # {"nome" : "vazio", "telefone": "vazio"} 

# * GET
contatos = {"ithallo@gmail.com": {"nome": "Ithallo", "idade": 20, "telefone": 40028922}}

# contatos["chave"]  # KeyError - não existe chave

contatos.get("chave")   # None
contatos.get("chave", {})   # {}
print(contatos.get("ithallo@gmail.com", {}))   # {'nome': 'Ithallo', 'idade': 20, 'telefone': 40028922}

# * POP
print(contatos.pop("ithallo@gmail.com", {}))    # Retorna o valor removido -> {'nome': 'Ithallo', 'idade': 20, 'telefone': 40028922}
print(contatos.pop("ithallo@gmail.com", "Já foi removido"))     # Retorna o valor default, se não acha a chave -> Já foi removido

# * POPITEM - Tira os itens na sequência, não recebe parâmetro
contatos = {"ithallo@gmail.com": {"nome": "Ithallo", "idade": 20, "telefone": 40028922}}
contatos.popitem()

# * SETDEFAULT -  setar um valor padrão para um chave
contatos = {"ithallo@gmail.com": {"nome": "Ithallo", "idade": 20, "telefone": 40028922}}

contatos.setdefault("nome", "Ithallo")      # Caso já criado, não altera, apenas os seguintes
contatos.setdefault("genero", "Masculino")      # Insere nova chave e valor com default

print(contatos)     # {'ithallo@gmail.com': {'nome': 'Ithallo', 'idade': 20, 'telefone': 40028922}, 'nome': 'Ithallo', 'genero': 'Masculino'}

# * UPDATE - Atualizar o dicionário
contatos.update({"ithallo@gmail.com": {"nome": "Ithallo Leandro"}})
print(contatos)     # {'ithallo@gmail.com': {'nome': 'Ithallo Leandro'}, 'nome': 'Ithallo', 'genero': 'Masculino'}

# * VALUES - Retornar todos os valores

# * DEL - Recebe o objeto a ser removido
del contatos["ithallo@gmail.com"]["telefone"]       # Remove o telefone


