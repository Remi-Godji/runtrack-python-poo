class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        # Affiche l'âge de la personne
        print("L'âge de la personne est :", self.age)

    def bonjour(self):
        # Affiche "Hello"
        print("Hello")

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


# Instanciation d'un objet de la classe Personne
personne = Personne()

# Instanciation d'un objet de la classe Eleve
eleve = Eleve()

# Affichage de l'âge de l'élève par défaut
eleve.afficherAge()