def retorna_maior(n):
    if n == 1:
        return int(input())
    return max(int(input()), retorna_maior(n - 1))

print(retorna_maior(10))