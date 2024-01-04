class Livre:
    def __init__(self, titre, auteur):
        self.__titre = titre
        self.__auteur = auteur
        self.__disponible = True  # Attribut privé pour la disponibilité du livre (par défaut : True)

    def vérification(self):
        return self.__disponible  # Vérifie si le livre est disponible (True) ou non (False)

    def emprunter(self):
        if self.vérification():  # Vérifie si le livre est disponible
            self.__disponible = False  # Rend le livre indisponible

    def rendre(self):
        if not self.vérification():  # Vérifie si le livre a été emprunté
            self.__disponible = True  # Rend le livre disponible
            # Création d'un livre avec un titre et un auteur
livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")

# Vérification de la disponibilité initiale du livre
print("Le livre est disponible :", livre.vérification())  # Affiche True (disponible)

# Emprunt du livre (si disponible)
livre.emprunter()

# Vérification de la disponibilité après l'emprunt
print("Le livre est disponible :", livre.vérification())  # Affiche False (indisponible)

# Rendre le livre (si emprunté)
livre.rendre()

# Vérification de la disponibilité après le rendu
print("Le livre est disponible :", livre.vérification())  # Affiche True (disponible)