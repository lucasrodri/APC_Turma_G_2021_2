#O volume de uma esfera com raio r é 4/3 \pi r^3.
#Qual é o volume de uma esfera com raio 5?

import math as m

#Entrada
raio = float(input("Informe o valor do raio: "))

#Computacao
volume = 4/3 * m.pi * (raio**3)

#Saida
print(f"O volume de uma esfera com raio 5 é: {volume:.2f}")