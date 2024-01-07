import math

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


class Cercle(Forme):
    def __init__(self, rayon):
        # Initialisation de l'attribut spécifique à la classe Cercle
        self.rayon = rayon

    def aire(self):
        # Surcharge de la méthode aire pour le cercle
        return math.pi * self.rayon ** 2


# Instanciation de la classe Rectangle avec une largeur de 5 et une hauteur de 3
rectangle = Rectangle(5, 3)

# Utilisation de la méthode aire de la classe Rectangle
print("Aire du rectangle :", rectangle.aire())

# Instanciation de la classe Cercle avec un rayon de 2
cercle = Cercle(2)

# Utilisation de la méthode aire de la classe Cercle
print("Aire du cercle :", cercle.aire())