import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conn = sqlite3.connect(ROOT / "bootcamp.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO tb01_cliente (NO_CLIENTE, EE_CLIENTE) VALUES (?, ?)', ('Teste1', "teste@email.com"))
    cursor.execute('INSERT INTO tb01_cliente (ID_CLIENTE, NO_CLIENTE, EE_CLIENTE) VALUES (?, ?, ?)', (1, 'Teste2', "teste2@email.com"))
    
    conn.commit()
    cursor.close()
except Exception as e:
    print(f"Erro: {e}")
    conn.rollback()     # Ao dar erro, o primeiro insert (Teste1) mesmo que esteja certo, também não será inserido

