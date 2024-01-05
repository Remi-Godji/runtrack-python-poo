class Ville:
    def __init__(self, nom, habitants):
        self.nom = nom
        self.habitants = habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.habitants += 1

# Création de l'objet Ville "Paris" avec 1 000 000 d'habitants
paris = Ville("Paris", 1000000)
print("Nombre d'habitants de Paris :", paris.habitants)

# Création de l'objet Ville "Marseille" avec 861 635 habitants
marseille = Ville("Marseille", 861635)
print("Nombre d'habitants de Marseille :", marseille.habitants)

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Ajout des nouvelles personnes à la population de leur ville respective
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

# Affichage du nombre d'habitants de Paris et de Marseille après l'arrivée des nouvelles personnes
print("Nombre d'habitants de Paris après l'arrivée des nouvelles personnes :", paris.habitants)
print("Nombre d'habitants de Marseille après l'arrivée des nouvelles personnes :", marseille.habitants)