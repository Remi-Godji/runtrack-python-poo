class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        # Initialisation des attributs spécifiques à la classe Vehicule
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        # Méthode pour afficher les informations générales du véhicule
        print("Marque :", self.marque)
        print("Modèle :", self.modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer(self):
        # Méthode pour démarrer le véhicule
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        # Appel au constructeur de la classe Vehicule avec les paramètres spécifiés
        super().__init__(marque, modele, annee, prix)
        # Ajout de l'attribut spécifique à la classe Voiture
        self.portes = 4

    def informationsVehicule(self):
        # Surcharge de la méthode informationsVehicule pour la classe Voiture
        # Appel à la méthode informationsVehicule de la classe Vehicule
        super().informationsVehicule()
        print("Nombre de portes :", self.portes)

    def demarrer(self):
        # Surcharge de la méthode demarrer pour la classe Voiture
        print("La voiture démarre go !!")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        # Appel au constructeur de la classe Vehicule avec les paramètres spécifiés
        super().__init__(marque, modele, annee, prix)
        # Ajout de l'attribut spécifique à la classe Moto
        self.roue = 2

    def informationsVehicule(self):
        # Surcharge de la méthode informationsVehicule pour la classe Moto
        # Appel à la méthode informationsVehicule de la classe Vehicule
        super().informationsVehicule()
        print("Nombre de roues :", self.roue)

    def demarrer(self):
        # Surcharge de la méthode demarrer pour la classe Moto
        print("La moto démarre  gooo !!")


# Instanciation d'un objet Voiture avec les informations spécifiées
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)

# Appel à la méthode informationsVehicule de la classe Voiture
voiture.informationsVehicule()

# Instanciation d'un objet Moto avec les informations spécifiées
moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)

# Appel à la méthode informationsVehicule de la classe Moto
moto.informationsVehicule()

# Appel à la méthode demarrer de la classe Voiture
voiture.demarrer()

# Appel à la méthode demarrer de la classe Moto
moto.demarrer()