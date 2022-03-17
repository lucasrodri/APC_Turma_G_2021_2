frase = input()
msg = ""
for palavra in frase.split():
    for c in palavra:
        msg += "p"+c
    msg += " "
print(msg)