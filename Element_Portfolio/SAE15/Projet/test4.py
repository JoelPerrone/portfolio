chaine = "08:00:00"
trois_premiers_chiffres = ''.join(char for char in chaine if char.isdigit())[:3]

print(trois_premiers_chiffres)
