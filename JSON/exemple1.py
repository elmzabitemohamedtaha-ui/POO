class Employe:
    def __init__(self,nom,prenom,salaire,numero):
        self.__nom=nom
        self.__prenom=prenom
        self.__salaire=salaire
        self.__numero=numero
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new
    @property
    def Prenom(self):
        return self.__prenom
    @Prenom.setter
    def Prenom(self,new):
        self.__prenom=new
    @property
    def Salaire(self):
        return self.__salaire
    @Salaire.setter
    def Salaire(self,new):
        self.__salaire=new
    @property
    def Numero(self):
        return self.__numero
    @Numero.setter
    def Numero(self,new):
        self.__numero=new
    def mondict(self):
        return{
            "nom":self.Nom,
            "prenom":self.Prenom,
            "salaire":self.Salaire,
            "numero":self.Numero
        }    
    def __str__(self):
        return f"{self.__nom}\t{self.__prenom}\t{self.__salaire}\t{self.__numero}"
class Societe:
    c=1
    def __init__(self,nom,adresse):
        self.code=Societe.c
        self.nom=nom
        self.adresse=adresse
        self.lemp=[]
        Societe.c+=1
    def Ajouter(self):
        saisie = 'Y'
        while saisie.upper() == 'Y':
            nom = input("taper le nom: ")
            prenom = input("taper le prenom: ")
            try:
                salaire = float(input("taper le salaire: "))
            except ValueError:
                print("Salaire invalide, valeur par défaut 0.0 utilisée.")
                salaire = 0.0
            try:
                numero = int(input("taper le numero: "))
            except ValueError:
                print("Numero invalide, valeur par défaut 0 utilisée.")
                numero = 0
            emp = Employe(nom, prenom, salaire, numero)
            self.lemp.append(emp)
            print("ajout avec succes")
            saisie = input("voulez-vous vraiment ajouter un employe Y/N: ")
    def Afficher(self):
        if not self.lemp:
            print("Aucun employe dans la societe.")
            return
        for e in self.lemp:
            print(e)
    
    def Supprimer(self,numero):
        for e in self.lemp:
            if e.Numero == numero:
                self.lemp.remove(e)
                print("suppression avec succes")
            else:
                print("Employe introuvable, suppression echouee")
    def Exporter(self):
        import json
        liste=[]
        for e in self.lemp:
            liste.append(e.mondict())
        with open("employes.json","w") as f:
            json.dump(liste,f,indent=4)
        print("exporter avec succes")
if __name__=="__main__":
    s1=Societe("OFPPT","Rabat")
    s1.Ajouter()
    s1.Afficher()
    num=int(input("taper le numero de l'employe a supprimer:"))
    s1.Supprimer(num)
    s1.Exporter()        
  

        
        
        
            
        
        
            
        
        
        
        
        
        