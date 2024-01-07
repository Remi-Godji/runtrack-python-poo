class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, nouvelle_hauteur):
        self.__hauteur = nouvelle_hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur


# Instanciation de la classe Rectangle
rectangle = Rectangle(5, 3)

# Utilisation des méthodes pour calculer le périmètre et la surface
print("Périmètre du rectangle :", rectangle.perimetre())
print("Surface du rectangle :", rectangle.surface())

# Utilisation des accesseurs pour obtenir la longueur et la largeur
print("Longueur du rectangle :", rectangle.get_longueur())
print("Largeur du rectangle :", rectangle.get_largeur())

# Utilisation des mutateurs pour modifier la longueur et la largeur
rectangle.set_longueur(7)
rectangle.set_largeur(4)

# Utilisation des méthodes avec les nouvelles valeurs
print("Périmètre du rectangle :", rectangle.perimetre())
print("Surface du rectangle :", rectangle.surface())

# Instanciation de la classe Parallelepipede
parallelepipede = Parallelepipede(5, 3, 2)

# Utilisation des méthodes pour calculer le périmètre, la surface et le volume du parallélépipède
print("Périmètre du parallélépipède :", parallelepipede.perimetre())
print("Surface du parallélépipède :", parallelepipede.surface())
print("Volume du parallélépipède :", parallelepipede.volume())