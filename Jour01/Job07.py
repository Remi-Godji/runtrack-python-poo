class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        return (self.x, self.y)
    # Création d'un personnage aux coordonnées (0, 0)
personnage = Personnage(0, 0)

# Déplacement du personnage
personnage.droite()
personnage.bas()


print(personnage.position())  