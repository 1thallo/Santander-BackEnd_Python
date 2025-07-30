import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent

conn = sqlite3.connect(ROOT / "bootcamp.sqlite")
cursor = conn.cursor()

# * CRIANDO TABELA
cursor.execute("DROP TABLE IF EXISTS tb01_cliente;")    # Um statement por vez
cursor.execute("""CREATE TABLE IF NOT EXISTS tb01_cliente (
    ID_CLIENTE  INTEGER PRIMARY KEY AUTOINCREMENT,
    NO_CLIENTE  VARCHAR(100),
    EE_CLIENTE  VARCHAR(100),
    CONSTRAINT UK01_TB01 UNIQUE (NO_CLIENTE));"""
)

# --
# * INSERINDO DADOS
dados = ("Ithallo", "ithallo@email.com")
cursor.execute("INSERT INTO tb01_cliente (NO_CLIENTE, EE_CLIENTE) VALUES (?, ?);", dados)

dados = ("Leandro", "leandro@email.com")
cursor.execute("INSERT INTO tb01_cliente (NO_CLIENTE, EE_CLIENTE) VALUES (?, ?);", dados)
conn.commit()

# --
# * ATUALIZANDO DADOS
def update_tabela(nome_tabela, nome_coluna, v_novo_valor, v_id):
    dados = (v_novo_valor, v_id)
    comando_sql = f"UPDATE {nome_tabela} SET {nome_coluna} = ? WHERE ID_CLIENTE = ?"
    cursor.execute(comando_sql, dados)
    conn.commit()

update_tabela("tb01_cliente", "EE_CLIENTE", "ithallo@gmail.com", 1)
update_tabela("tb01_cliente", "NO_CLIENTE", "Ithallo Leandro", 1)

# --
# * DELETANDO DADOS
def deletar_registros(v_nome_tabela, v_id):
    comando_sql = f"DELETE FROM {v_nome_tabela} WHERE ID_CLIENTE = ?"
    cursor.execute(comando_sql, (v_id,))
    conn.commit()

deletar_registros("tb01_cliente", 2)

# --
# * INSERIR VÁRIOS - Versão Ithallo Ultra Pro Max ☝️🥸
def inserir_varios(nome_tabela, dados_lista, nomes_colunas):
    """
    Insere múltiplos registros na tabela.
    
    Args:
        nome_tabela (str): Nome da tabela
        dados_lista (list): Lista de tuplas com os dados a inserir
        nomes_colunas (str): String com nomes das colunas ex: "(NO_CLIENTE, EE_CLIENTE)"
    """
    # conta os placeholders
    num_colunas = len(nomes_colunas.strip("()").split(","))
    placeholders = ", ".join(["?" for _ in range(num_colunas)])
    
    comando_sql = f"INSERT INTO {nome_tabela} {nomes_colunas} VALUES ({placeholders})"
    cursor.executemany(comando_sql, dados_lista)
    conn.commit()

dados_para_inserir = [("João Silva", "joao@email.com"),("Maria Sato", "maria@email.com"), ("Pedro Melo", "pedro@email.com")]

inserir_varios("tb01_cliente", dados_para_inserir, "(NO_CLIENTE, EE_CLIENTE)")

# --
# * CONSULTA REGISTROS - fetch
def consulta_por_nome(nome_tabela, nome_coluna, valor_coluna):
    comando_sql = f"SELECT * FROM {nome_tabela} WHERE 1=1 AND {nome_coluna} LIKE '%' || ? || '%'"
    cursor.execute(comando_sql, (valor_coluna,))
    return cursor.fetchall()

print(consulta_por_nome("tb01_cliente", "NO_CLIENTE", "Ithallo"))

cursor.close()
conn.close()

