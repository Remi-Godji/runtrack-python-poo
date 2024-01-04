class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0      
        self.__level = self.__student_eval()  # Appelle la méthode privée pour définir le niveau initial

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def student_info(self):
        print("Nom:", self.__nom)
        print("Prénom:", self.__prenom)
        print("Identifiant:", self.__numero_etudiant)
        print("Niveau:", self.__level)

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(30)
john_doe.add_credits(60)
john_doe.add_credits(20)

# Impression des informations de l'étudiant
john_doe.student_info()
