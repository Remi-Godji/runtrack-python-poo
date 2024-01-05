class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Détail du compte :")
        print("Numéro de compte :", self.__numero_compte)
        print("Titulaire :", self.__prenom, self.__nom)
        print("Solde :", self.__solde)

    def afficherSolde(self):
        print("Solde du client :", self.__solde)

    def versement(self, montant):
        self.__solde += montant
        print("Versement de", montant, "effectué.")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__solde + (self.__decouvert * montant) >= montant:
            self.__solde -= montant
            print("Retrait de", montant, "effectué.")
            self.afficherSolde()
        else:
            print("Montant indisponible. Retrait impossible.")

    def agios(self, taux):
        if self.__solde < 0:
            montant_agios = self.__solde * taux
            self.__solde += montant_agios
            print("Appliquer des agios de", montant_agios, "au solde.")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde + (self.__decouvert * montant) >= montant:
            self.retrait(montant)
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Montant indisponible. Virement impossible.")

# Création du premier compte bancaire avec découvert autorisé
compte1 = CompteBancaire("123456", "Doe", "John", 1000, decouvert=True)

# Création du deuxième compte bancaire à découvert
compte2 = CompteBancaire("654321", "Smith", "Alice", -500, decouvert=True)

# Affichage des détails des deux comptes
compte1.afficher()
compte2.afficher()

# Versement de 500 du premier compte vers le deuxième compte à découvert
compte1.virement(compte2, 500)