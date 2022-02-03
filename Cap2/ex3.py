"""
Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um
certo passo (8min15s por quilômetro), então 3 quilômetros a um
passo mais rápido (7min12s por quilômetro) e 1 quilômetro no
mesmo passo usado em primeiro lugar, que horas chego em casa
para o café da manhã?
"""

km = 1
minutos = 8
segundos = 15
total_s = ((minutos*60) + segundos) * km

km = 3
minutos = 7
segundos = 12
total_s += ((minutos*60) + segundos) * km

km = 1
minutos = 8
segundos = 15
total_s += ((minutos*60) + segundos) * km

hora = 6
minutos = 52
total_s += (hora*3600) + (minutos*60)

hora = total_s // 3600
minutos = (total_s % 3600) // 60
segundos =  (total_s % 3600) % 60

print(f"Chego em casa para o café da manhã às {hora}:{minutos}:{segundos}")

