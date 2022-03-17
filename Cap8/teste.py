"""
linha = "+"+"-"*15+("+"+"-"*10)*6+"+"
#linha = "+---------------+----------+----------+----------+----------+----------+----------+"
dias = "|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |"

print(f"{linha}\n{dias}\n{linha}")

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

h1 = ["CIC0116L","","CIC0116L",""]
h2 = []


for linha in m:
    print(linha)
    for e in linha:
        print(e)
"""
a1 = "Lucas rodrigues Costa"
a2 = "Lucas Rodrigues Costa"
soma = 0
for i in a1:
    soma += ord(i)
print(soma)
soma = 0
for i in a2:
    soma += ord(i)
print(soma)
