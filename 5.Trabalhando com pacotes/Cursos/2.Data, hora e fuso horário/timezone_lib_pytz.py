import pytz
import datetime

data = datetime.datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)     # 2025-07-17 06:46:39.286471+02:00
print(data2)    # 2025-07-17 01:48:07.274173-03:00 

