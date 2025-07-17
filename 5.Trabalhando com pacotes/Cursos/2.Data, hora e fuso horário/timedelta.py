# Timedelta -> operações matemáticas com datas
from datetime import *

data = datetime(2025, 10, 1, 14, 55, 10)
print(data)     # 2025-10-01 14:55:10

data_mais_uma_semana = data + timedelta(weeks=1)
print(data_mais_uma_semana)     # 2025-10-08 14:55:10

# ------------------------------------------------------
# Caso de uso: Lava jato
tipo_carro = 'P' # "M", "G"
tempo_carro_p = 30
tempo_carro_m = 45
tempo_carro_g = 60

data_atual = datetime.now()

if tipo_carro == 'P':
    estimativa_lavagem = data_atual + timedelta(minutes=tempo_carro_p)
    print(f"Entrada: {data_atual}\nEstimativa de saída: {estimativa_lavagem}")
elif tipo_carro == 'M':
    estimativa_lavagem = data_atual + timedelta(minutes=tempo_carro_m)
    print(f"Entrada: {data_atual}\nEstimativa de saída: {estimativa_lavagem}")
else:
    estimativa_lavagem = data_atual + timedelta(minutes=tempo_carro_g)
    print(f"Entrada: {data_atual}\nEstimativa de saída: {estimativa_lavagem}")