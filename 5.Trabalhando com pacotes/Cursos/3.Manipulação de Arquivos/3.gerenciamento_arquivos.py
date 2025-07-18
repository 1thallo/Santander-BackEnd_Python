import os, shutil

root_path = os.path.dirname(__file__)

# * os.mkdir(f"{root_path}/novo_diretorio.py")

# ** os.rename(f"{root_path}/novo_diretorio.py",
#           f"{root_path}/novo_diretorio")

# arquivo = open(f"{root_path}/gerenciamento.txt", "w")

# shutil.move(f"{root_path}/gerenciamento.txt",
#             f"{root_path}/novo_diretorio")

os.remove(f"{root_path}/gerenciamento.txt")