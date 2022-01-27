#Quantas milhas há em X (entrada do usuário em real) quilômetros?
#Dica: uma milha equivale a 1,61 quilômetro.

#Entrada
km = float(input("Entre com a quantidade de quilômetros: "))

#Computacao
result = km/1.61

#Saída
print(f"Em {km} quilômetros temos {result:.2f} milhas")
#print("Em", km ,"quilômetros temos", "{:.2f}".format(result), "milhas")