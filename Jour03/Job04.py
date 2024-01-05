class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print("Statistiques du joueur", self.nom)
        print("Numéro :", self.numero)
        print("Position :", self.position)
        print("Buts marqués :", self.buts_marques)
        print("Passes décisives :", self.passes_decisives)
        print("Cartons jaunes :", self.cartons_jaunes)
        print("Cartons rouges :", self.cartons_rouges)


class EquipeDeFoot:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherEffectif(self):
        print("Effectif de l'équipe", self.nom)
        for joueur in self.joueurs:
            print(joueur.nom)

    def afficherStatistiquesEquipe(self):
        print("Statistiques de l'équipe", self.nom)
        for joueur in self.joueurs:
            joueur.afficherStatistiques()


# Création de joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Isagi Yoichi", 11, "Milieu")
joueur3 = Joueur("Modric", 10, "Milieu")

# Création d'une équipe de foot
equipe = EquipeDeFoot("Real Madrid")

# Ajout des joueurs à l'équipe
equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)

# Affichage de l'effectif de l'équipe
equipe.afficherEffectif()

# Actions des joueurs pendant un match
joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur3.recevoirUnCartonRouge()

# Affichage des statistiques de l'équipe
equipe.afficherStatistiquesEquipe()