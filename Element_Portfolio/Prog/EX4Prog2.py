class Produit:
    def __init__(self, nom="", desc="", ref="", prix=0.0, catégorie=""):
        self.nom = nom
        self.desc = desc
        self.ref = ref
        self.prix = prix
        self.catégorie = catégorie

class Magasin:
    def __init__(self, nom="", loca="", nEmployé=0, tabProd=[]):
        self.nom = nom
        self.loca = loca
        self.nEmployé = nEmployé
        self.tabProd = tabProd
    
    def ajouterProduit(self, newProd):
        self.tabProd.append(newProd)
    
    def supprProduit(self, ProduitEp):
        self.tabProd.remove(ProduitEp)
    
    def __repr__(self):
        return repr(f"{self.nom}")
    
    def somme_Produit(self):
        somme = 0
        for p in self.tabProd:
            somme += p.prix
        return somme


Groupe = [Magasin("MAG1", "4 rue pu pret", 15, [Produit("perceuse", "pour percer", "142648", 30.0, "bricolage"), Produit("tournevis", "viser les vis", "843185", 20.0, "bricolage")]), Magasin("MAG2", "6 allée de l'arnaque", 3, [Produit("piano", "instrument très populaire", "15684321", 250.0, "instrument à corde"), Produit("batterie", "instrument permettant de donner le rythme", "5678415", 50.0, "instrument à percussion")]), Magasin("MAG3", "74 boulevard du jura", 1, [Produit("Burger", "plat allemand", "41684", 15.0, "plat principal"), Produit("Gaspacho", "soupe froide", "4861559", 20.0, "entrée")])]
#print(sorted(Groupe, key=lambda Magasin : Magasin.nEmployé))

print(sorted(Groupe, key=lambda Magasin : Magasin.somme_Produit()))