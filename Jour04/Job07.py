import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        # Crée un paquet de 52 cartes avec différentes valeurs et couleurs
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        return paquet

    def melanger_paquet(self):
        # Mélange le paquet de cartes
        random.shuffle(self.paquet)

    def tirer_carte(self):
        # Tire une carte du paquet, si le paquet n'est pas vide
        if len(self.paquet) == 0:
            print("Le paquet est vide.")
            return None
        else:
            return self.paquet.pop()

class Blackjack:
    def __init__(self):
        self.joueur_main = []
        self.croupier_main = []
        self.jeu = Jeu()

    def distribuer_cartes(self):
        # Distribue 2 cartes à chaque joueur (joueur et croupier) au début de la partie
        for _ in range(2):
            self.joueur_main.append(self.jeu.tirer_carte())
            self.croupier_main.append(self.jeu.tirer_carte())

    def afficher_main(self, main, joueur=True):
        # Affiche la main du joueur ou du croupier
        print("Main du Joueur:" if joueur else "Main du Croupier:")
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def calculer_total(self, main):
        # Calcule le total des points dans une main, en tenant compte des valeurs des cartes
        total = 0
        as_count = 0

        for carte in main:
            if carte.valeur in ['J', 'Q', 'K']:
                total += 10
            elif carte.valeur == 'A':
                as_count += 1
                total += 11
            else:
                total += int(carte.valeur)

        # Gère les As pour éviter de dépasser 21
        while total > 21 and as_count:
            total -= 10
            as_count -= 1

        return total

    def joueur_tirer_carte(self):
        # Le joueur tire une carte supplémentaire
        self.joueur_main.append(self.jeu.tirer_carte())

    def jouer(self):
        # Fonction principale pour jouer une partie de Blackjack
        self.jeu.melanger_paquet()
        self.distribuer_cartes()

        while True:
            self.afficher_main(self.joueur_main)
            choix = input("Voulez-vous tirer une carte ? (Oui/Non): ").lower()

            if choix == 'oui':
                self.joueur_tirer_carte()
                total_joueur = self.calculer_total(self.joueur_main)

                # Vérifie si le joueur a dépassé 21
                if total_joueur > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    break
            else:
                break

        total_croupier = self.calculer_total(self.croupier_main)

        # Le croupier tire des cartes jusqu'à ce qu'il atteigne au moins 17 points
        while total_croupier < 17:
            self.croupier_main.append(self.jeu.tirer_carte())
            total_croupier = self.calculer_total(self.croupier_main)

        # Affiche les mains du joueur et du croupier
        self.afficher_main(self.joueur_main)
        self.afficher_main(self.croupier_main, joueur=False)

        # Détermine le résultat de la partie
        if total_joueur > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
        elif total_croupier > 21 or total_joueur > total_croupier:
            print("Félicitations, vous avez gagné!")
        elif total_joueur == total_croupier:
            print("Égalité.")
        else:
            print("Le croupier a gagné.")

# Exécution du jeu
partie = Blackjack()
partie.jouer()
