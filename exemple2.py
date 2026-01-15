import json

class Employe:
    def __init__(self, prenom, age, salaire):
        self.__prenom = prenom
        self.__age = age
        self.__salaire = salaire

    @property
    def Prenom(self):
        return self.__prenom

    @Prenom.setter
    def Prenom(self, new):
        self.__prenom = new

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, new):
        self.__age = new

    @property
    def Salaire(self):
        return self.__salaire

    @Salaire.setter
    def Salaire(self, new):
        self.__salaire = new

    def salaireNet(self, taux=20):
        salairenet=self.__salaire-(self.__salaire*taux/100)
        
        return salairenet

    def todict(self):
        mondict= {
            "prenom": self.Prenom,
            "age": self.Age,
            "salaire": self.Salaire,
            "salaireNet": self.salaireNet()
        }
        return mondict
        

    def __str__(self):
        return f"{self.Prenom}\t{self.Age}\t{self.Salaire}\t{self.salaireNet()}"


class Entreprise:
    c = 1

    def __init__(self, nom, ville):
        self.code = Entreprise.c
        self.nom = nom
        self.ville = ville
        self.Lemp = []
        Entreprise.c += 1

    def ajouter(self, emp):
        if emp in self.Lemp:
            print("employe existant")
        else:
            self.Lemp.append(emp)
            print("ajouter avec succes")

    def afficher(self):
        print(f"{self.code}\t{self.nom}\t{self.ville}")
        print("les employes")
        print("prenom\tage\tsalaire\tSalaireNet")
        for emp in self.Lemp:
            print(f"{emp.Prenom}\t{emp.Age}\t{emp.Salaire}\t{emp.salaireNet()}")

    def exporter(self):
        newlist=[]
        for emp in self.Lemp:
            newlist.append(emp.todict())
        with open("employe.json","w") as F:
            json.dump(newlist, F, indent=2)
        print("exporter avec succes")
if __name__ == "__main__":
    e1 = Employe("taha", 30, 15000)
    e2 = Employe("ilyas", 25, 12000)
    e3 = Employe("mohamed", 28, 13000)

    ent = Entreprise("OFPPT", "Rabat")
    ent.ajouter(e1)
    ent.ajouter(e2)
    ent.ajouter(e3)
    ent.afficher()
    ent.exporter()