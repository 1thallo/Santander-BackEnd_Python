import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conn = sqlite3.connect(ROOT / "bootcamp.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o ID do cliente\n=> ")

cursor.execute(f"SELECT * FROM tb01_cliente WHERE ID_CLIENTE = {id_cliente}") # Tudo isso por não ter um placeholder

clientes = cursor.fetchall()
for cliente in clientes:
    print(dict(cliente))

"""
----------------------------------------------------------------------------------------
Informe o ID do cliente
=> 1 OR 1=1
{'ID_CLIENTE': 1, 'NO_CLIENTE': 'Ithallo Leandro', 'EE_CLIENTE': 'ithallo@gmail.com'}
{'ID_CLIENTE': 3, 'NO_CLIENTE': 'João Silva', 'EE_CLIENTE': 'joao@email.com'}
{'ID_CLIENTE': 4, 'NO_CLIENTE': 'Maria Sato', 'EE_CLIENTE': 'maria@email.com'}
{'ID_CLIENTE': 5, 'NO_CLIENTE': 'Pedro Melo', 'EE_CLIENTE': 'pedro@email.com'}
----------------------------------------------------------------------------------------

- ⚠️⚠️ Input = True, retornou todos os registros na tabela de clientes (vazamento de dados)
"""