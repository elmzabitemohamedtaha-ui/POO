import json
class Etudiant:
    def __init__(self,n,nom,f,nt):
        self.__numero=n
        self.__nom=nom
        self.__filiere=f
        self.__note=nt

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, value):
        self.__numero = value

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, value):
        self.__nom=value

    @property
    def filiere(self):
        return self.__filiere
    @filiere.setter
    def filiere(self, value):
        self.__filiere=value
    
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self,value):
        self.__note=value

    def toDict(self):
        mondict={
            "numero":self.numero,
            "nom":self.nom,
            "filiere":self.filiere,
            "noteExam":self.note,
            "resultat":self.appreciation()
        }
        return mondict
    
    def appreciation(self):
        n=self.__note
        if n<10:
            return "redouble"
        elif n>=9 and n<10:
            return"rachete"
        else:
            return"admis"
    
    def __str__(self):
        return f"{self.__numero}\t{self.__nom}\t{self.__filiere}\t{self.__note}\t{self.appreciation()}"
class Universite:
    c=1
    def __init__(self,n,v):
        self.code=Universite.c
        self.nom=n
        self.ville=v
        self.Letd=[]
        Universite.c+=1
    
    def ajouter(self,etd):
      if etd in self.Letd:
          print("etudiant deja existant")
      else:
          self.Letd.append(etd)
          print("ajouter avec succes")

    def supprimer(self,etd:Etudiant):
        if etd in self.Letd:
            rep=bool(int(input("voulez-vous vraiment supprimer ? 1=oui/0=non")))
            if rep:
                self.Letd.remove(etd)
                print("suppeimer avec succes")
            else:
                print("suppression annuler")
        else:
            print("etudiant n'existe pas")

    def afficher(self):
        print(f"{self.code}\t{self.nom}\t{self.ville}")
        print("Liste des etudiants")
        print("Numero\tNom\tFiliere\tNote\tAppreciation")
        m=0
        n=len(self.Letd)
        for s in self.Letd:
            print(s)
            m=m+s.note
        moyenne=m/n
        print(f"Moyenne:{moyenne}")

    def exporter(self):
        newListe=[]
        for etd in self.Letd:
            newListe.append(etd.toDict())
        with open("etudiants.json","w") as F:
            json.dump(newListe,F)
        print("exporter avec succes")

if __name__=="__main__":
    et1=Etudiant(1,"taha","dev",17.59)
    et2=Etudiant(2,"ilyas","des",15.24)
    et3=Etudiant(3,"mohamed","dev",16.54)
    u1=Universite("Mohammed5","Rabat")
    u1.ajouter(et1)
    u1.ajouter(et2)
    u1.ajouter(et3)
    u1.afficher()
    u1.exporter()