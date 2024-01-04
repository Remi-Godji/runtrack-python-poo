class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats commandés
        self.__statut_commande = "en cours"  # Statut de la commande (par défaut : en cours)

    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats_commandes:  # Vérifie si le plat n'est pas déjà dans la commande
            self.__plats_commandes[nom_plat] = {"prix": prix, "statut": self.__statut_commande}  # Ajoute le plat à la commande

    def annuler_commande(self):
        self.__plats_commandes = {}  # Annule la commande en supprimant tous les plats

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            total += plat["prix"]  # Ajoute le prix de chaque plat au total
        return total

    def afficher_commande(self):
        print("Numéro de commande :", self.__numero_commande)
        for nom_plat, plat in self.__plats_commandes.items():
            print("Plat :", nom_plat, "- Prix :", plat["prix"], "- Statut :", plat["statut"])
        print("Total à payer :", self.__calculer_total())

    def calculer_tva(self, taux):
        tva = self.__calculer_total() * taux
        return tva
    
    # Création d'une commande avec un numéro de commande
commande = Commande("CMD001")

# Ajout de plats à la commande
commande.ajouter_plat("Pizza Margherita", 10.99)
commande.ajouter_plat("Burger Cheese", 8.99)
commande.ajouter_plat("Salade César", 6.99)

# Affichage de la commande
commande.afficher_commande()

# Calcul de la TVA avec un taux de 20%
tva = commande.calculer_tva(0.2)
print("TVA :", tva)

# Annulation de la commande
commande.annuler_commande()

# Affichage de la commande après annulation
commande.afficher_commande()