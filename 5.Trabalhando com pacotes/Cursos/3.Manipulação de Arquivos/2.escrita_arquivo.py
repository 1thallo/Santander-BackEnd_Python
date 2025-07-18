import os

current_dir = os.path.dirname(__file__)

# WRITE()
file = open(f"{current_dir}/exemplo_escrita.txt", "w")
file.write("Ola mundo!")
file.writelines(["\n", "Escrevendo ", "um ", "novo ", "texto!"])
file.close()