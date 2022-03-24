nFatias, fatiaPremiada = map(int, input().split())
bolo = [False] * nFatias
bolo[fatiaPremiada] = True
"""
pedacoNormal = False
pedacoPremiado = True
for fatia in range(nFatias):
    if fatia == fatiaPremiada:
        bolo.append(pedacoPremiado)
    else:
        bolo.append(pedacoNormal)
"""

while nFatias > 0:
    nome,fatia = input().split()
    fatia = int(fatia)
    if bolo.pop(fatia):
        ganhador = nome
    nFatias -= 1

print(ganhador)
    