import re 
#class pour les Formateurs
class Formateur:
    def __init__(self,code,nom,prenom,sexe,naissance,specialite):
        motif=r"^[0-9]{5}$"
        ver=re.search(motif,str(code))
        if ver:
            self._code=code
            self._nom=nom
            self._prenom=prenom
            self._sexe=sexe
            self._naissance=naissance
            self._specialite=specialite
        else:
            raise erreurCode("le code doit contenir 5 chiffres ")
    #les accesseurs et les mutateurs
    @property
    def Code(self):
        return self._
    @Code.setter
    def Code(self,new):
        motif=r"^[0-9]{5}$"
        
        ver=re.search(motif,str(new))
        if ver:
            self._code=new
        else:
            raise erreurCode("Le code doit contenir 5 chiffres")
    @property
    def Nom(self):
        return self._nom
    @Nom.setter
    def Nom(self,new):
        self._nom=new
    
    @property
    def Prenom(self):
        return self._prenom
    @Prenom.setter
    def Prenom(self,new):
        self._prenom=new

    @property
    def Sexe(self):
        return self._sexe
    @Sexe.setter
    def Sexe(self,new):
        self._sexe=new

    @property
    def Naissance(self):
        return self._naissance
    @Naissance.setter
    def Naissance(self,new):
        self._naissance=new

    @property
    def Specialite(self):
        return self._specialite
    @Specialite.setter
    def Specialite(self,new):
        self._specialite=new
    
    def Afficher(self):
        print(f"code :{self._code} \t Nom:{self._nom} \t Prenom:{self._prenom} \t sexe:{self._sexe} \t naissaance:{self._naissance} \t specialite:{self._specialite}")


#La class d'exception       
class erreurCode(Exception):
    pass
#class pour les stagiaires
class Stagiaire:
    cde=1
    def __init__(self,nom,prenom,niveau):
        self.__code=Stagiaire.cde
        self.__nom=nom
        self.__prenom=prenom
        self.__niveau=niveau
        Stagiaire.cde+=1
    
    def Afficher(self):
        print(f"{self.__code}\t{self.__nom}\t{self.__prenom}\t{self.__niveau}")

class Parrin(Formateur):
    def __init__(self,code,nom,prenom,sexe,naissance,specialite):
        super().__init__(code,nom,prenom,sexe,naissance,specialite)
        self.Lstg=[]
    def Afficher(self):
        super().Afficher()
        print("Stagiaires parrainés")
        if not self.Lstg:
            print("Aucun stagiaire ")
        else:
            for s in self.Lstg:
                s.Afficher()
    def AjouterStagiaire(self,stg):
        if stg in self.Lstg:
            print("Stagiaire deja existe ")
        else:
            self.Lstg.append(stg)
    def SupprimerStagiaire(self,stg):
        if stg in self.Lstg:
            self.Lstg.remove(stg)
        else:
            print("Stagiaire introuvable ")

if __name__=="__main__":
    try:
        p1=Parrin("12345","salim","raji","M",2005,"dev")
        s1=Stagiaire("Mohamed","Taha","ST")
        s2=Stagiaire("Adam","Bahja","LW")
        p1.AjouterStagiaire(s1)
        p1.AjouterStagiaire(s2)
        p1.Afficher()
    except erreurCode as e:
        print(f"Erreur : {e}")