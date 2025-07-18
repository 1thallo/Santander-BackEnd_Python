import os

script_dir = os.path.dirname(__file__)
arquivo_path = os.path.join(script_dir, 'lorem.txt')

file = open(arquivo_path, 'r')
# print(file.read())

# * READLINE e READLINES
# readline() retorna uma linha por vez em sequencia
# readlines() retorna uma lista onde cada elemento é uma linha do arquivo

# print(file.readline())
print(file.readlines())
file.close()


