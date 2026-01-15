class Employe:
    def __init__(self,NU,N,S):
        self.__numero=NU
        self.__nom=N
        self.__service=S
    @property
    def Numero(self):
        return self.__numero
    @Numero.setter
    def Numero(self,new):
        self.__numero=new
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new
    @property
    def Service(self):
        return self.__service
    @Service.setter
    def Service(self,new):
        self.__service=new
    def __str__(self):
        return f"{self.__numero}\t{self.__nom}\t{self.__service}"
class Entreprise:
    c=1
    def __init__(self,nom,adresse):
        self.code=Entreprise.c
        self.nom=nom
        self.adresse=adresse
        self.Lemp=[]
        Entreprise.c+=1
    def Ajouter(self):
        saisie="Y"
        while saisie=="Y":
            num=int(input("Taper le numero : "))
            nom=input("Taper le nom : ")
            service=input("Taper le service : ")
            emp=Employe(num,nom,service)
            self.Lemp.append(emp)
            print("Ajout avec succes ")
            saisie=(input(" voulez-vous ajouter un autre employe? Y/N"))
    def Afficher(self):
        print(f"{self.code}\t{self.nom}\t{self.adresse}")
        print("Listes des employes :")
        print("Numero \t Nom \t Service ")
        for e in self.Lemp:
            print(e)
        print(f"il y a {len(self.Lemp)} employes ")
    def Rechercher(self,num):
        for e in self.Lemp:
            if e.Numero==num:
                return e
        return None
    def Supprimer(self,num):
        e=self.Rechercher(num)
        if e is not None:
            self.Lemp.remove(e)
            print("Suppression avec succes")
        else:
            print("Employe n'existe pas")
if __name__=='__main__':
    ent=Entreprise("TechCorp","123 Rue Principale")
    ent.Ajouter()
    ent.Afficher()
    num_rech=int(input("Taper le numero de l'employe a rechercher : "))
    emp=ent.Rechercher(num_rech)
    if emp is not None:
        print("Employe trouve :")
        print(emp)
    else:
        print("Employe n'existe pas")
    num_sup=int(input("Taper le numero de l'employe a supprimer : "))
    ent.Supprimer(num_sup)
    ent.Afficher()   
    
        
        