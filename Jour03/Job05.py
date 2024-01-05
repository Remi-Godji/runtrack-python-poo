class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        print(f"{self.nom} attaque {adversaire.nom}")
        adversaire.vie -= 10
        print(f"{adversaire.nom} perd 10 points de vie")

    def estEnVie(self):
        return self.vie > 0


class Jeu:
    def __init__(self):
        self.niveau = None

    def choisirNiveau(self):
        niveaux_possibles = ["facile", "normal", "difficile"]
        while True:
            niveau = input("Choisissez le niveau (facile, normal, difficile) : ")
            if niveau in niveaux_possibles:
                self.niveau = niveau
                break
            else:
                print("Niveau invalide. Veuillez réessayer.")

    def lancerJeu(self):
        self.choisirNiveau()

        if self.niveau == "facile":
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == "normal":
            vie_joueur = 100
            vie_ennemi = 100
        elif self.niveau == "difficile":
            vie_joueur = 150
            vie_ennemi = 150

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print("Le combat commence !")

        while joueur.estEnVie() and ennemi.estEnVie():
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

        if joueur.estEnVie():
            print("Vous avez vaincu l'ennemi !")
        else:
            print("Vous avez été vaincu par l'ennemi !")


# Création d'un objet Jeu
jeu = Jeu()

# Lancement du jeu
jeu.lancerJeu()