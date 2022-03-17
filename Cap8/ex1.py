frase = input()
msg = ""
for palavra in frase.split():
    msg += palavra[2]
print(msg)