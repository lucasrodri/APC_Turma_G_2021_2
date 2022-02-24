from datetime import datetime
#now = datetime.now()
#dd/mm/YY H:M:S
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)


def oi2():
    """
    Essa funcao serve para retornar a string "Oi"
    """
    return "Oi"

def oi(nome, sobrenome = "Rodrigues" , ultimoNome = "Costa"):
    def oi3():
        return "Hello"
    print(ss)
    now = datetime.now()
    hora_atual = now.strftime("%H:%M:%S")
    f = oi3
    return f"Olá {nome} {sobrenome} {ultimoNome}", hora_atual, f

#a = oi("Lucas")
ss = "Adriana"
msg,hora,fucao_nova = oi("Lucas","Rodrigues","Costaaaaa")

if fucao_nova == oi2:
    print(True)
else:
    print(False)
    
print(oi2())
print(fucao_nova())

print(msg,hora)

print("Teste","de Souza",sep="|",end=" KKKK ")
print("Teste","de Souza",sep="|")

"""
maior = float('-inf')
a = int(input())
if a > maior:
    maior = a
    
a = int(input())
if a > maior:
    maior = a
    
a = int(input())
if a > maior:
    maior = a
    
print(maior)
"""

maior = float('-inf')
for i in range(3):
    a = int(input())
    if a > maior:
        maior = a
print(maior)




