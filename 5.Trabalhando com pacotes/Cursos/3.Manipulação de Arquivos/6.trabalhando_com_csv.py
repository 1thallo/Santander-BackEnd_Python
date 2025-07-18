import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH / 'usuarios.csv', 'w', newline = '', encoding='UTF-8') as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(['id','nome'])
#         escritor.writerow(['1','Ithallo'])
#         escritor.writerow(['2','Leandro'])
# except IOError as e:
#     print(f"Erro ao manipular o arquivo: {e}")

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', newline='', encoding='UTF-8') as arquivo:
        leitor = csv.reader(arquivo)
        for dado in leitor:
            print(dado)
except IOError as e:
    print(f"Erro ao manipular o arquivo: {e}")