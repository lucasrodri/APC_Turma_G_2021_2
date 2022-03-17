frase = input()
msg = ""
for c in frase:
    if c.isupper():
        msg += "U"
    elif c.islower():
        msg += "L"
    elif c.isdigit():
        msg += "D"
    elif c.isspace():
        msg += "W"
print(msg)