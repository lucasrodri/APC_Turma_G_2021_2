
def ordena(a,b,c):
    if a > b and a > c:
        if b > c:
            return a,b,c
        else:
            return a,c,b
    elif b > a and b > c:
        if a > c:
            return b,a,c
        else:
            return b,c,a
    else:
        if a > b:
            return c,a,b
        else:
            return c,b,a

a = int(input())
b = int(input())
c = int(input())

a,b,c = ordena(a,b,c)

#print(a,b,c)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a == b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or c == a:
    print("TRIANGULO ISOSCELES")
else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")
