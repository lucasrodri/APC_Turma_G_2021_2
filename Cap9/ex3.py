jogo = []

def lerJogo(n):
    while n > 0:
        linha = input().split()
        jogo.append(linha)
        n -= 1

def exibeJogo():
    for linha in jogo:
        print(*linha)


def atuaGravidade():
    for linha in range(len(jogo)-2,-1,-1):
        for coluna in range(len(jogo[linha])):
            if jogo[linha][coluna] == "o":
                if jogo[linha+1][coluna] == ".":
                    jogo[linha+1][coluna] = "o"
                    jogo[linha][coluna] = "."

n = int(input())
lerJogo(n)
atuaGravidade()
exibeJogo()