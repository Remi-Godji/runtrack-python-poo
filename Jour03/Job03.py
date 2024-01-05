class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "terminée"

    def __str__(self):
        return f"Titre : {self.titre}\nDescription : {self.description}\nStatut : {self.statut}"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, tache):
        self.taches.remove(tache)

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list


# Création de plusieurs instances de Tache
tache1 = Tache("Faire les courses", "Acheter du lait et des œufs", "à faire")
tache2 = Tache("Appeler le plombier", "Fixer une date de rendez-vous", "à faire")
tache3 = Tache("Préparer la réunion", "Préparer l'ordre du jour et les documents", "terminée")

# Création de la liste de tâches
liste_taches = ListeDeTaches()

# Ajout des tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de toutes les tâches
liste_taches.afficherListe()

# Suppression d'une tâche
liste_taches.supprimerTache(tache2)

# Modification du statut d'une tâche
tache1.marquerCommeFinie()

# Affichage des tâches restantes
taches_a_faire = liste_taches.filterListe("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(tache)