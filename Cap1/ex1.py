#Quantos segundos há em X (entrada do usuário em inteiro) minutos e
#Y (entrada do usuário em inteiro) segundos?

#Entrada
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))

#Computacao
result = m*60 + s

#Saída
print(f"Em {m} minutos e {s} segundos temos {result} segundos")