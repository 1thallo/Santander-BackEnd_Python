from datetime import *

data = datetime.now()
print(data)     # 2025-07-17 00:32:45.370042

# Formatação de data e hora
print(data.strftime("%d/%m/%Y %H:%M"))  # 17/07/2025 00:32

# conversão string para datetime
data_string = "01/10/2004 13:38"
data_convertida = datetime.strptime(data_string,"%d/%m/%Y %H:%M")
print(data_convertida)      # 2004-10-01 13:38:00

# --------------------------------------------------------------
# Exemplo: Máscara PT-BR
datetime_atual = datetime.now()
datetime_string = "17/07/2025 02:15"
mascara_ptbr = "%d/%m/%Y %H:%M"

print(datetime_atual.strftime(mascara_ptbr))    # 17/07/2025

conversao = datetime.strptime(datetime_string, mascara_ptbr)
print(conversao)        # 2025-07-17 02:15:00