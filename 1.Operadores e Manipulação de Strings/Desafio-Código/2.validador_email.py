"""
Descrição
Uma empresa quer validar se os e-mails cadastrados pelos usuários estão no formato correto. 
Crie uma função que receba um e-mail e verifique se ele é válido, seguindo as regras:

📌 Regras para um e-mail válido:
- Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.
- Não pode começar ou terminar com "@".
- Não pode conter espaços.

Entrada
Uma string contendo o e-mail a ser validado.

Saída
"E-mail válido" se o e-mail estiver no formato correto.
"E-mail inválido" caso contrário.
"""

# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
if '@' not in email:
  print('E-mail inválido')
elif email.startswith('@') or email.endswith('@'):
  print('E-mail inválido')
elif ' ' in email:
  print('E-mail inválido')
elif 'gmail.com' not in email and 'outlook.com' not in email:
  print('E-mail inválido')
else:
  print('E-mail válido')