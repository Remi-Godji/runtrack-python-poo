class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        # Affiche l'âge de la personne
        print("L'âge de la personne est :", self.age)

    def bonjour(self):
        # Affiche "Bonjour les gars"
        print("Bonjour les gars")

    def modifierAge(self, nouvel_age):
        # Modifie l'âge de la personne
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        # Affiche "Je vais en cours"
        print("Je vais en cours")

    def afficherAge(self):
        # Affiche "J'ai XX ans", où XX est l'âge de l'élève
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        # Attribut privé pour indiquer la matière enseignée par le professeur
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        # Affiche "Le cours va commencer"
        print("Le cours va commencer")


# Instanciation d'un objet de la classe Eleve
eleve = Eleve()

# Faire dire "Bonjour les gars" à l'élève
eleve.bonjour()

# Faire dire "Je vais en cours" à l'élève
eleve.allerEnCours()

# Redéfinir l'âge de l'élève à 15 ans
eleve.modifierAge(15)

# Création d'un objet Professeur
professeur = Professeur(age=40)

# Faire dire "Bonjour les gars" au professeur
professeur.bonjour()

# Commencer le cours grâce à la méthode enseigner du professeur
professeur.enseigner()