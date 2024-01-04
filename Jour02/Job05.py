# Déclaration de la classe Voiture
class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.est_en_marche = False
        self.reservoir = 50

    def demarrer(self):
        if self.reservoir > 5:
            self.est_en_marche = True
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer. Le réservoir est trop bas.")

    def arreter(self):
        self.est_en_marche = False
        print("La voiture s'arrête.")

# Exemple d'utilisation de la classe Voiture
ma_voiture = Voiture("Toyota", "Camry", 2022, 15000)

# Vérification de l'état initial
print("En marche:", ma_voiture.est_en_marche)

# Tentative de démarrage
ma_voiture.demarrer()

# Vérification de l'état après démarrage
print("En marche:", ma_voiture.est_en_marche)

# Arrêt de la voiture
ma_voiture.arreter()