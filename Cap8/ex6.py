frases = input()
msg = ""
for frase in frases.split("."):
    if frase != "":
        msg += frase.strip().capitalize() + ". "
print(msg)