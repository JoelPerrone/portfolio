import numpy as np #J'importe la bibliothèque numpy et je l'a nomme comme "np"
#print(np.pi) #je demande d'afficher la valeur de pi selon la bibliothèque "np"

#On veut créer un tableau :

#a = np.array([1,2,3,4]) #je définit un tableau("array" en anglais) avec comme valeur 1, 2, 3 et 4 que je stocke dans la variable "a"
#print(a) #J'affiche le résultat
#print(type(a)) #Je demande le type de la variable "a"

#Numpy agit comme une liste basique de python :
#print(a[0]) #je demande d'afficher le premier élément de la liste
#print(a[1]) #Je demande d'afficher le deuxième élément de la liste

#Création d'un tableau :
#b = np.array([[1,2,3,4], [5,6,7,8]]) #Je définit deux lignes de 4 valeurs chacune et je les stocke dans la variable "b".
#print(b[1,2])

m = np.arange(2,20,2)
print(m)