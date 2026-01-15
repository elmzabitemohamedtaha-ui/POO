import re
class Etudiant:
    def __init__(self, numero, nom, age):
        motif="[0-9]{10}"
        verif=re.search(motif,str(numero))
        motif="[A-Z]+"
        verif2=re.search(motif,str(nom))
        
        if verif and verif2:
            self.__numero=str(numero)
            self.__nom=nom
            self.__age=age
        else:
            raise Exception("le numero doivent etre contient 10 chiffres ou le nom doit etre en majuscule")
    
    @property
    def Numero(self):
        return self.__numero

    @property
    def Nom(self):
        return self.__nom

    @property
    def Age(self):
        return self.__age
    def __str__(self):
        return f"Etudiant {self.__numero}: {self.__nom}, Age: {self.__age}"
class Etablissement(Etudiant):
    
    def __init__(self,nometab):
        super().__init__(str(num), nom, age)
        self.name=nometab
        self.letd=[]
    def Ajouter(self,etd):
        if etd is not  self.letd :
            self.letd.append(etd)
        else:
            print("cette etudiants est deja existant")
    def Afficher(self):
        print("les stagiaires :")
        for etd in self.letd:
            print(f"{self.__numero}\t NOM:{self.__nom}\t AGE:{self.__age}")
    def Supprimer(self,etd):
        if etd in self.letd:
            self.letd.remove(etd)
        else:
            print("l'etudiant n'est pas dans la liste")
    def __eq__(self, value):
        if isinstance
    
            
        
if __name__ == '__main__':
    try:
        num=int(input("taper le numero :"))
        nom=input("taper le nom:")
        age=int(input("taper l'age:"))
        etud=Etudiant(num,nom,age)
        print(etud)
    except Exception as e:
        print(f"Erreur: {e}")
    nometab=input("taper le nom de l'etablissement:")
    etab=Etablissement(nometab)
    etab.Ajouter(etud)
    etab.Afficher()