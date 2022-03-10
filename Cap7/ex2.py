n = int(input())
maximo = float("-inf")
minimo = float("inf")
while n > 0:
    x,y = input().split()
    x,y = [int(x), int(y)]
    soma = 0
    while y > 0:
        if x%2 == 0:#par
            x += 1
        else:#impar
            soma += x
            x += 2
            y -= 1
    print(soma)
    if soma > maximo:
        maximo = soma
    if soma < minimo:
        minimo = soma
    n-=1
print(maximo,minimo,sep="\n")
print(f"{(maximo+minimo)/2:.2f}")
    