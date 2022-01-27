#Se você correr X (entrada do usuário em real) quilômetros em
#Y (entrada do usuário em real) minutos e Z (entrada do usuário em int)
#segundos, Qual é a sua velocidade média em milhas por hora?

#Entrada
km = float(input("Quantos quilômetros você correu: "))
minutos = int(input("Em quantos minutos: "))
segundos = int(input("E em quantos segundos: "))

#Computacao
#Solução: Robson Lima
milhas = km/1.61
segundos = minutos*60 + segundos
hora = segundos/3600
velocidade = milhas/hora

#velocidade = (km/1.61) / ((minutos*60 + segundos) / 3600)

#Saída
print(f"A sua velocidade média em milhas por hora é: {velocidade:.2f}")