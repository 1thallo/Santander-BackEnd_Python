def mensagem(nome):
    print("Executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
    print("Executando função de execução!")
    return funcao(nome)

print(executar(mensagem, "Ithallo"))
"""
Executando função de execução!
Executando mensagem
Oi Ithallo"""

print(executar(mensagem_longa, "Ithallo"))
"""
Executando função de execução!
Executando mensagem longa
Olá tudo bem com você Ithallo?
"""