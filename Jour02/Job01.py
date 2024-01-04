class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé pour la longueur
        self.__largeur = largeur    # Attribut privé pour la largeur

    def getLongueur(self):
        return self.__longueur  # Accesseur pour obtenir la longueur

    def setLongueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur  # Mutateur pour modifier la longueur

    def getLargeur(self):
        return self.__largeur  # Accesseur pour obtenir la largeur

    def setLargeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur  # Mutateur pour modifier la largeur

        # Création du rectangle avec une longueur de 10 et une largeur de 5
rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
print("Longueur :", rectangle.getLongueur())  # Affiche la longueur initiale
print("Largeur :", rectangle.getLargeur())    # Affiche la largeur initiale

# Modification des valeurs
rectangle.setLongueur(8)  # Modifie la longueur du rectangle
rectangle.setLargeur(3)   # Modifie la largeur du rectangle

# Affichage des nouvelles valeurs
print("Nouvelle longueur :", rectangle.getLongueur())  # Affiche la nouvelle longueur
print("Nouvelle largeur :", rectangle.getLargeur())    # Affiche la nouvelle largeur