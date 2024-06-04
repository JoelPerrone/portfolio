unePhrase = input("Saisir une phrase : ")
unePhrase = unePhrase.lower()
if unePhrase[::-1] == unePhrase:
    print(unePhrase, "est un palindrome.")
else:
    print(unePhrase, "n'est pas un palindrome. Preuve", unePhrase[::-1])
