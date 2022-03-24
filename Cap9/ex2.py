nbrinquedos = int(input())
brinquedos = input().split()
brinquedos_originais = brinquedos[:]
dias = 5
while dias > 0:
    brinquedo,orientacao,casas = input().split()
    casas = int(casas)
    index = brinquedos.index(brinquedo)
    brinquedos.pop(index)
    if orientacao == "D":
        index += casas
        if index >= nbrinquedos:
            index = nbrinquedos - 1
        brinquedos.insert(index,brinquedo)
    else:
        index -= casas
        if index < 0:
            index = 0
        brinquedos.insert(index,brinquedo)
    dias -= 1

soma = 0
for index in range(nbrinquedos):
    if brinquedos[index] != brinquedos_originais[index]:
        soma += 1
print(soma)