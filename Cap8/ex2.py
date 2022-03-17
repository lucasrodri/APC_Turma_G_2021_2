frase = input()
msg = ""
for palavra in frase.split():
    msg += palavra[1::2] + " "
print(msg[:-1])