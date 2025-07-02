# OLD STYLE %
nome = "Ithallo"
idade = 20
profissao = "Programador"
linguagem = "Python"

print("Ola, me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculado no Bootcamp, cursando %s." % (nome, idade, profissao, linguagem))

# METODO FORMAT
print("Ola, me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculado no Bootcamp, cursando {}.".format(nome, idade, profissao, linguagem))

print("Ola, me chamo {1}. Tenho {0} anos de idade, trabalho como {3} e estou matriculado no Bootcamp, cursando {2}.".format( idade, nome, linguagem, profissao))

print("Ola, me chamo {var1}. Tenho {var2} anos de idade, trabalho como {var3} e estou matriculado no Bootcamp, cursando {var4}.".format(var1=nome, var2=idade, var4=linguagem, var3=profissao))

# F-STRING
print(f"Ola, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no Bootcamp, cursando {linguagem}.")

# FORMATAR COM F-STRING
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")  #3.14
print(f"Valor de PI: {PI:10.2f}")  #        3.14
