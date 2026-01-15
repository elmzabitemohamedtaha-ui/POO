# =========================
# Classe Employe
# =========================
class Employe:
    def __init__(self, matricule=0, nom="", prenom="", adresse="",
                 genre="", age=0.0, service="", departement="", ville=""):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.genre = genre
        self.age = age
        self._service = service
        self._departement = departement
        self.ville = ville

    def __str__(self):
        return (
            f"Matricule: {self.matricule}\n"
            f"Nom: {self.nom}\n"
            f"Prenom: {self.prenom}\n"
            f"Adresse: {self.adresse}\n"
            f"Genre: {self.genre}\n"
            f"Age: {self.age}\n"
            f"Service: {self._service}\n"
            f"Departement: {self._departement}\n"
            f"Ville: {self.ville}"
        )


# ===A
# Classe Mission

class Mission:
    def __init__(self, numero=0, libelle="", lieu="", commentaire="", montant=0.0):
        self.numero = numero
        self.libelle = libelle
        self.lieu = lieu
        self.commentaire = commentaire
        self.montant = montant

    def calculer_charge(self):
        return self.montant

    def __str__(self):
        return (
            f"Numero: {self.numero}\n"
            f"Libellé: {self.libelle}\n"
            f"Lieu: {self.lieu}\n"
            f"Commentaire: {self.commentaire}\n"
            f"Montant: {self.montant}"
        )



# Exception personnalisée

class MontantException(Exception):
    def __init__(self, message="Le montant doit être entre 10 et 500"):
        super().__init__(message)

# Classe OrdreMissionTrain

class OrdreMissionTrain(Mission):
    def __init__(self, numero=0, libelle="", lieu="", commentaire="",
                 montant=0.0, employe=None, type_train="", classe=1):

        if montant < 10 or montant > 500:
            raise MontantException()

        super().__init__(numero, libelle, lieu, commentaire, montant)

        self.employe = employe
        self.type_train = type_train
        self.classe = classe

    # Méthode polymorphe
    def calculer_charge(self):
        return self.montant * self.classe

    def __str__(self):
        return (
            "----- Ordre de Mission Train -----\n"
            f"{super().__str__()}\n"
            f"Type de train: {self.type_train}\n"
            f"Classe: {self.classe}\n"
            f"Employé:\n{self.employe}\n"
            f"Charge: {self.calculer_charge()}"
        )


# =========================
# Classe ListeMissions
# =========================
class ListeMissions:
    def __init__(self):
        self.missions = []

    def ajouter(self, mission):
        self.missions.append(mission)
        print("Mission ajoutée avec succès ✅")

    def afficher(self):
        print("===== Liste des Missions =====")
        for mission in self.missions:
            print(mission)
            print("----------------------------")


# =========================
# Exemple d'utilisation
# =========================
if __name__ == "__main__":
    try:
        emp = Employe(
            1, "Dupont", "Ali", "Rue 12",
            "Homme", 30, "IT", "Informatique", "Paris"
        )

        mission_train = OrdreMissionTrain(
            numero=101,
            libelle="Déplacement pro",
            lieu="Lyon",
            commentaire="Réunion",
            montant=100,
            employe=emp,
            type_train="TGV",
            classe=2
        )

        liste = ListeMissions()
        liste.ajouter(mission_train)
        liste.afficher()

    except MontantException as e:
        print("Erreur :", e)


