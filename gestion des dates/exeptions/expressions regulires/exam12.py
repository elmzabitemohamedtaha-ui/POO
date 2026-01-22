import re
import json
class Stagiaire:
    def __init__(self,num,nom,prenom):
        motif="^[0-9]{7}$"
        verif=re.search(motif,str(num))
        if verif: 
            self.__numero=num
            self.__nom=nom
            self.__prenom=prenom
        else:
            raise Exception("le numero doit contient 7 numero")
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
    def Prenom(self):
        return self.__prenom
    @Prenom.setter
    def Prenom(self,new):
        self.__prenom=new
    def Todict(self):
        return {"numero":12,
                "nom":"mohamed taha",
                "prenom":"cr7"
                }
    def __eq__(self, value):
        return self.__numero==value.__numero
    def __str__(self):
        return f"{self.__numero}:{self.__nom}{self.__prenom}"
class Etablissememt:
    def __init__(self,nomett):
        
        self.__nomett=nomett
        self.Lmembres=[]
    @property
    def NomEtt(self):
        return self.__nomett
    @NomEtt.setter
    def NomEtt(self,new):
        self.__nomett=new
    def Nombresmembre(self):
        return len(self.Lmembres)
    def Indice(self,membre):
        if membre in self.Lmembres:
            return self.Lmembres.index(membre)
    def Ajouter(self,membre):
        if membre in self.Lmembres:
            self.Lmembres.append(membre)
            return True
        else:
            return False
    def Afficher(self):
        print("les stagiaires:")
        print(f"Ettablissement:{self.__nomett}")
        print(f"Nombres des membres:{self.Nombresmembre()}")
    def Suprimmer(self,m):
        
        if m in self.Lmembres:
            self.Lmembres.remove(m)
        else:
            print("membre introuvable")
    def Exporter(self):
        newlist=[]
        for membre in self.Lmembres:
            newlist.append(membre.Todict())
        with open("membre.json","w") as f:
            json.dump(newlist,f)
        print("exporter avec succes")
if __name__=='__main__':
    s1=Stagiaire(1234567,"mohamed","taha")
    s2=Stagiaire(2345678,"imane","barkaoui")
    s3=Stagiaire(3456789,"aissam","alaoui")
    s4=Stagiaire(4567890,"badr","moubtassim")
    ett=Etablissememt("OFPPT")
    ett.Ajouter(s1)

    ett.Ajouter(s2)
    ett.Ajouter(s3)
    ett.Afficher()
    ett.Suprimmer(s4)
    ett.Exporter()

            
        
        
        
    
            
        
    
        
    
        
        
    
        