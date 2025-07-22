"""
Descrição
Uma empresa deseja criar um sistema simples de login para permitir acesso de funcionários. O sistema precisa verificar se o usuário 
está cadastrado e se a senha informada está correta.

Entrada
O programa recebe duas linhas de entrada:
- Primeira linha: Nome do usuário cadastrado.
- Segunda linha: Senha correspondente ao usuário.

Saída
"Acesso permitido" se as credenciais estiverem corretas.
"Usuário ou senha incorretos" caso contrário.
"""

# Dicionário com usuários cadastrados e suas senhas
usuarios = {
    "joao": "1234",
    "ana": "abcd",
    "maria": "senha123",
    "marcelo": "iou789",

}

# Entrada do usuário
usuario = input().strip()
senha = input().strip()

# TODO: Verifique se o usuário existe e a senha está correta:
if usuario in usuarios and usuarios[usuario] == senha:
  print("Acesso permitido")
else:
    print("Usuário ou senha incorretos")
  