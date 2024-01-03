class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

mon_animal = Animal()
print("L'âge de l'animal : " + str(mon_animal.age))

mon_animal.vieillir()
print(mon_animal.age)

mon_animal.nommer("sukuna")
print ("mon animal s'appelle "+ str(mon_animal.prenom))