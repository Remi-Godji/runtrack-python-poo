class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        # Étape 1: Initialiser les attributs privés
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages

    # Étape 2: Assesseurs (Getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nombre_pages(self):
        return self.__nombre_pages

    # Étape 3: Mutateurs (Setters)
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nombre_pages(self, nouveau_nombre_pages):
        # Vérifier si le nouveau nombre de pages est un entier positif
        if isinstance(nouveau_nombre_pages, int) and nouveau_nombre_pages > 0:
            self.__nombre_pages = nouveau_nombre_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Étape 4: Méthode pour afficher les informations
    def afficher_infos(self):
        print("Titre :", self.__titre)
        print("Auteur :", self.__auteur)
        print("Nombre de pages :", self.__nombre_pages)

# Étape 5: Tester les fonctionnalités de la classe
if __name__ == "__main__":
    # Création d'un livre
    livre1 = Livre("Harry Potter", "J.K. Rowling", 350)

    # Affichage des informations initiales
    print("Informations initiales du livre:")
    livre1.afficher_infos()

    # Modification du titre et de l'auteur
    livre1.set_titre("Nouveau Titre")
    livre1.set_auteur("Nouvel Auteur")

    # Tentative de modification du nombre de pages avec une valeur incorrecte
    livre1.set_nombre_pages(-100)

    # Modification du nombre de pages avec une valeur correcte
    livre1.set_nombre_pages(400)

    # Affichage des informations mises à jour
    print("\nInformations mises à jour du livre:")
    livre1.afficher_infos()
