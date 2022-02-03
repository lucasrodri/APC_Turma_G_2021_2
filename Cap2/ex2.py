#Suponha que o preço de capa de um livro seja R$ 24,95, mas as
#livrarias recebem um desconto de 40%.
#O transporte custa R$ 3,00 para o primeiro exemplar e
#75 centavos para cada exemplar adicional.
#Qual é o custo total de atacado para 60 cópias?

#Entrada
valor_livro = float(input("Informe o valor do livro (R$): "))
desconto = float(input("Informe o valor do desconto (Ex.: 40): "))
transporte = float(input("Informe o valor do transporte do primeiro exemplar (R$): "))
transporte_a = float(input("Informe o valor do transporte de cada exemplar adicional (R$): "))
copias = int(input("Informe o número de cópias: "))

#Computacao
valor_do_livro = valor_livro * (1 - (desconto/100))
valor_do_transporte = transporte + transporte_a*(copias-1)
custo_total = (valor_do_livro*copias) + valor_do_transporte

#Saida
print(f"O custo total de atacado para {copias} cópias é: R${custo_total:.2f}")


