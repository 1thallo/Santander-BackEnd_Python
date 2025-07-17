from datetime import datetime, timezone, timedelta

data_tempo_oslo = datetime.now(timezone(timedelta(hours=2)))
data_tempo_sp = datetime.now(timezone(timedelta(hours=-3)))

print(data_tempo_oslo)      # 2025-07-17 06:51:33.812463+02:00
print(data_tempo_sp)        # 2025-07-17 01:51:33.812472-03:00

