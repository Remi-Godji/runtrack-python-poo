class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Résultat de l'addition : {resultat}")

# Instancier la classe Operation
operation_instance = Operation(nombre1=5, nombre2=5)

# Appeler la méthode addition et afficher le résultat en console
operation_instance.addition()
