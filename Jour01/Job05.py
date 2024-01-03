class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée horizontale (x) : {self.x}")

    def afficherY(self):
        print(f"Coordonnée verticale (y) : {self.y}")

    def changerX(self, nouvelle_valeur_x):
        self.x = nouvelle_valeur_x

    def changerY(self, nouvelle_valeur_y):
        self.y = nouvelle_valeur_y
# Instancier un objet Point avec les coordonnées par défaut (0, 0)
point1 = Point()

# Afficher les coordonnées du point
point1.afficherLesPoints()

# Changer la valeur de x et y
point1.changerX(5)
point1.changerY(10)

# Afficher les nouvelles coordonnées du point
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
