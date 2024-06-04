import numpy as np 
untableau = np.genfromtxt("C:\\Users\\joelp\\documents\\BUT - RT\\1ere Année\\Cours\\SAE15\\Base numpy\\iris.csv", delimiter=";", skip_header=True)
#On importe un fichier avec la méthode de numpy "genfromtxt", on précise son chemin. avec la varibale delimiter nous dit quel signe sépare les valeurs entre elles et
#skip_header forme qu'on ne prends pas en compte la première ligne.
print(untableau)

