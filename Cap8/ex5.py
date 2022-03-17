n = int(input())
somaP = 0
somaU = 0
while n > 0:
    frase = input()
    for c in frase:
        if c.lower() == "p":
            somaP += 1
        if c.lower() == "u":
            somaU += 1
    n -= 1
print(somaP,somaU)
