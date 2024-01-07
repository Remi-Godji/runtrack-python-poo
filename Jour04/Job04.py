class Forme:
    def aire(self):
        # Méthode pour calculer l'aire de la forme (initialisée à 0)
        return 0


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        # Initialisation des attributs spécifiques à la classe Rectangle
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        # Surcharge de la méthode aire pour le rectangle
        return self.largeur * self.hauteur


# instanciation de la classe Rectangle avec une largeur de 5 et une hauteur de 3
rectangle = Rectangle(5, 3)

# Utilisation de la méthode aire de la classe Rectangle
print("Aire du rectangle :", rectangle.aire())