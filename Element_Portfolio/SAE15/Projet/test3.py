chaine = "abc123xyz456"
deux_premiers_chiffres = ''
for char in chaine:
    if char.isdigit():
        deux_premiers_chiffres += char
    elif deux_premiers_chiffres:
        break

deux_premiers_chiffres = int(deux_premiers_chiffres)
print(deux_premiers_chiffres)