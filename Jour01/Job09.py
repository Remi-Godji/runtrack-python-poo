class Produit:
    def __init__(self, nom, prix_HT, TVA):
        self.nom = nom
        self.prix_HT = prix_HT
        self.TVA = TVA

    def calculer_prix_TTC(self):
         return self.prix_HT + (self.prix_HT * self.TVA)


    def afficher(self):
        infos = f"Nom : {self.nom}\n" \
                f"Prix HT : {self.prix_HT} euros\n" \
                f"TVA : {self.TVA}\n" \
                f"Prix TTC : {self.calculer_prix_TTC()} euros"
        return infos

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix_HT):
        self.prix_HT = nouveau_prix_HT

    def obtenir_nom(self):
        return self.nom

    def obtenir_prix(self):
        return self.prix_HT

    def obtenir_TVA(self):
        return self.TVA

# Création des produits
produit1 = Produit("Chemise", 39.99, 0.1)
produit2 = Produit("Chaussures", 79.99, 0.15)

# Affichage des informations des produits
print(produit1.afficher())
print(produit2.afficher())

# Modification du nom et du prix du produit 1
produit1.modifier_nom("Nouvelle chemise")
produit1.modifier_prix(49.99)

# Modification du nom et du prix du produit 2
produit2.modifier_nom("Nouvelles chaussures")
produit2.modifier_prix(89.99)

# Affichage des nouveaux prix des produits
print("Nouveau prix du produit 1 :", produit1.calculer_prix_TTC())
print("Nouveau prix du produit 2 :", produit2.calculer_prix_TTC())
