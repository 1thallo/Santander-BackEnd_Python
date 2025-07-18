from pathlib import Path
import os

"""Mais comuns: 
_> FileNotFoundError: Arquivo nao pode ser encontrado no diretorio especificado
_> PermissionError: Tentativa de abrir um arquivo sem as permissões adequadas r ou w
_> IOError: Erro geral de E/S ao trabalhar com um arquivo
_> UnicodeDecodeError: Tentiva inadequada de decodificar dados de um arquivo
_> UnicodeEncodeError: Tentar codificar dados em uma determinada codificacao ao gravar em um arquivo de texto
_> IsADirectoryError: Tentativa de abrir um diretório em vez de um arquivo de texto"""

# root_path = Path(__file__).parent
root_path = os.path.dirname(__file__)

try:
    file = open("arquivo_inexistente.py", "r")
except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado\n{e}")

try:
    file = open(f"{root_path}/novo_diretorio")
except IsADirectoryError as e:
    print(f"Impossível abrir um diretório: {e}")
except PermissionError as e:
    print(f"Permissão Negada ao tentar abrir diretório!")
