import numpy as np #J'ajoute la bibliothéque "numpy" que je renomme en "np"
import pandas as pa #J'ajoute aussi la bibliothéque de pandas que je renomme "pa"

def AfficheSalleUtilisée(): #Je crée la fonction "AfficheSalleUtilisée"
    ListeSalle = [] #Je crée la liste "ListeSalle"
    planningEDT = pa.read_csv('C:\\Users\\joelp\\Documents\\BUT-RT\\1A\\Cours\\SAE15\\Projet\\joel_mod.csv', usecols=["Groups","Location"])
    listeTPGlobal = ['TP1', 'TP2', 'TP3', 'TP4', 'TP5']
    #J'importe le fichier "joel_mod.csv", je fais apparaître seulement les éléments de la colonne "Location" que je place dans la variable "planningEDT"
    for index, row in planningEDT.iterrows(): #Je crée une boucle "for" ou je cherche chaque éléments de la colonne "location" de la variable "planningEDT"
        if row['Groups'] in listeTPGlobal: #Je vérifie si l'élément de la colonne "Groups" est présent dans la liste "listeTPGlobal"
            ListeSalle.append(row["Location"]) #Si c'est vrai, je rajoute la salle dans la liste "ListeSalle"
    #Je rajoute chaque éléments à la liste "ListeSalle"
    listeSallesSansDoublons = list(set(ListeSalle)) #Je crée la liste "ListeSallesSansDoublons" ou je lui attribue le contenu de la liste "ListeSalle" en supprimant les doublons
    print(listeSallesSansDoublons) #J'affiche le résultat
        
def coursGeneraux(choix): #Je crée la fonction "AfficheCoursGeneral"
    rapportEDT = pa.read_csv('C:\\Users\\joelp\\Documents\\BUT-RT\\1A\\Cours\\SAE15\\Projet\\joel_mod.csv',usecols=["HStart", "HEnd", "Groups", "Location"],index_col=3)
    #Je crée la variable "rapportEDT" à laquelle je lui attribu le contenu du fichier 'joel.csv', je n'affiche que les colone "Hdébut", "HFin", "Groupes" et "Localisation"
    #et je définit la colone 'localisation' comme étant celle qui servira d'index
    return rapportEDT.loc[choix] #Je retourne le tableau selon la valeur de l'argument passé en paramètre

def convPandasNumpy(tab): #Je crée une nouvelle fonction "conversionPandasNumy"
    Tableau = np.array(coursGeneraux(tab)) #J'attribue la variable "Tableau" comme la conversion du résultat de la fonction "afficheCoursGeneral"
    return Tableau #Je retourne la variable "Tableau"

def CalculHoraireParSalle(ligne): #je crée une nouvelle fonction "CalculHoraireParSalle"
    for cpt in convPandasNumpy(ligne): #Je fais une boucle par ligne 
        debutCours = cpt[0] #Je place la valeur de l'element de la première colonne première comme étant l'heure de début de cours
        troiPreChifDeb = debutCours.join(char for char in debutCours if char.isdigit())[:3] 
        #Je récupère les 3 premiers chiffres de la chaîne de caractère "debutCours" et je le place dans la varibale "troiPreChifDeb"
        finCours = cpt[1] #Je définit la variable "finCours" comme étant le contenu de la 2ème colonne
        troiPreChifFin = finCours.join(element for element in finCours if element.isdigit())[:3]
        #Je récupère les 3 premiers chiffres de la variable "finCours" et je les place dans la variable "troiPreChifFin"
        if cpt[2] == 'TP1': #Si dans la colonne "Groups", il y a marqué 'TP1' ...
            listeTP1 = [] #Je crée la liste "TP1"
            if troiPreChifDeb[2] == '3': #Si le dernier des trois premiers chiffres de l'heure de début est le chiffre 3
                convFloDeb = float(troiPreChifDeb[:2]) + 0.5 #Je récupére les deux premiers chifres que je convertit en décimal et je rajoute 0.5
                if troiPreChifFin[2] == '3': #Si le dernier des trois premiers chiffres de l'heure de fin est le chiffre 3
                    convFloFin = float(troiPreChifFin[:2]) + 0.5 #Je récupére les deux premiers chifres que je converti en décimal et je lui additionne 0.5
                else: #Sinon 
                    convFloFin = float(troiPreChifFin[:2]) #Je récupère simplement les deux premiers chiffres que je convertit en décimal
            else: #Sinon 
                convFloDeb = float(troiPreChifDeb[:2]) #Je récupère simplement les deux premiers chiffres que je converti en décimal
                if troiPreChifFin[2] == '3': #Si le dernier des trois chiffres de l'heure de fin est le chiffre 3
                    convFloFin = float(troiPreChifFin[:2]) + 0.5 #Alors je récupère les 2 premiers chiffres, je converti en décimal et je rajoute 0.5
                else: #Sinon
                    convFloFin = float(troiPreChifFin[:2]) #Je récupère simplement les deux premiers chiffres de l'heure de fin
            difTP1 = convFloFin - convFloDeb #Je fait la diffèrence entre l'heure de fin et l'heure de début
            listeTP1.append(difTP1) #J'ajoute les heures de cours du TP1 dans la liste "listeTP1"
            #Ensuite la logique reste la même pour tout les TP
        if cpt[2] == 'TP2':
            listeTP2 = []
            if troiPreChifDeb[2] == '3':
                convFloDeb = float(troiPreChifDeb[:2]) + 0.5
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            else:
                convFloDeb = float(troiPreChifDeb[:2])
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            difTP2 = convFloFin - convFloDeb
            listeTP2.append(difTP2)
        if cpt[2] == 'TP3':
            listeTP3 = []
            if troiPreChifDeb[2] == '3':
                convFloDeb = float(troiPreChifDeb[:2]) + 0.5
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            else:
                convFloDeb = float(troiPreChifDeb[:2])
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            difTP3 = convFloFin - convFloDeb
            listeTP3.append(difTP3)
        if cpt[2] == 'TP4':
            listeTP4 = []
            if troiPreChifDeb[2] == '3':
                convFloDeb = float(troiPreChifDeb[:2]) + 0.5
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            else:
                convFloDeb = float(troiPreChifDeb[:2])
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            difTP4 = convFloFin - convFloDeb
            listeTP4.append(difTP4)
        else:
            listeTP5 = []
            if troiPreChifDeb[2] == '3':
                convFloDeb = float(troiPreChifDeb[:2]) + 0.5
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            else:
                convFloDeb = float(troiPreChifDeb[:2])
                if troiPreChifFin[2] == '3':
                    convFloFin = float(troiPreChifFin[:2]) + 0.5
                else:
                    convFloFin = float(troiPreChifFin[:2])
            difTP5 = convFloFin - convFloDeb
            listeTP5.append(difTP5)
    horaireTP1 = sum(listeTP1) #Je définit la variable "horaireTP1" comme étant la somme de tout les heure de cours de la liste "listeTP1"
    horaireTP2 = sum(listeTP2) #Je définit la variable "horaireTP2" comme étant la somme de tout les heure de cours de la liste "listeTP2"
    horaireTP3 = sum(listeTP3) #Je définit la variable "horaireTP3" comme étant la somme de tout les heure de cours de la liste "listeTP3"
    horaireTP4 = sum(listeTP4) #Je définit la variable "horaireTP4" comme étant la somme de tout les heure de cours de la liste "listeTP4"
    horaireTP5 = sum(listeTP5) #Je définit la variable "horaireTP5" comme étant la somme de tout les heure de cours de la liste "listeTP5"
    horaireGlobale = horaireTP1 + horaireTP2 + horaireTP3 + horaireTP4 + horaireTP5 #Je déinit la variable "horaireGloable" comme étant la somme de tout les TP
    print(f"La salle {ligne} est utilisée en tout {horaireGlobale}h, dont {horaireTP1}h par le TP1, {horaireTP2}h par le TP2, {horaireTP3}h par le TP3, {horaireTP4}h par le TP4 et {horaireTP5}h par le TP5")
    #Une phrase finale est affichée sur l'écran en répondant aux attentes du projet.

#AfficheSalleUtilisée()
CalculHoraireParSalle('B7')