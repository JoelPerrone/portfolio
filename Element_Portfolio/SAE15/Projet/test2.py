import numpy as np #J'ajoute la bibliothéque "numpy" que je renomme en "np"
import pandas as pa #J'ajoute aussi la bibliothéque de pandas que je renomme "pa"

def afficheCoursTP(choix1, choix2): #Je crée la fonction "AfficheCoursTp"
    rapportEDT = pa.read_csv('C:\\Users\\joelp\\Documents\\BUT-RT\\1A\\Cours\\SAE15\\Projet\\joel_mod.csv', usecols=["HStart", "HEnd", "Groups", "Location"], index_col=2)
    #Je crée la variable "rapportEDT" à laquelle je lui attribu le contenu du fichier 'joel.csv', je n'affiche que les colone "Hdébut", "HFin", "Groupes" et "Localisation"
    print(rapportEDT.loc[[choix1, choix2]])

afficheCoursTP('TP1','TDA')