from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "lorem.txt", "r") as arquivo:     # Fecha o arquivo automaticamente
    print("Trabalhando com o arquivo")

print(arquivo.read())       # I/O operation on closed file

# --------------- Arquivo inexistente

try:
    with open(ROOT_PATH / "lllorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as e:
    print(f"Erro: {e}")

# ---------------- Codificação

try:
    with open(ROOT_PATH / "arquivo_utf8", "w", encoding='UTF-8') as arquivo:
        arquivo.write("Codificação correta é importante!")
except IOError as e:
    print(f"Erro: {e}")