
def retorna_primeiro_e_maior(n,primeiro = None, maior=float("-inf")):
    """
    Leia n numeros e retorna o primeiro lido e o maior deles
    """
    if n == 0:
        return primeiro,maior
    else:
        a = int(input())
        
        if primeiro == None:
            primeiro = a
        
        if a > maior:
            maior = a
        return retorna_primeiro_e_maior(n-1,primeiro,maior)

primeiro, maior = retorna_primeiro_e_maior(10)

if maior%primeiro == 0:
    print(maior)
    print(primeiro)
else:
    print(maior)
