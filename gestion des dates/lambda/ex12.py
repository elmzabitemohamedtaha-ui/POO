from abc import ABC , abstractmethod
class ObjetPostal(ABC):
    def __init__(self,n,adr,cdep,ville,exp):
        self._nom=n
        self._adresse=adr
        self._code=cdep
        self._ville=ville
        self._expedite=exp

    @property
    def Nom(self):
        return self._nom
    @Nom.setter
    def Nom(self,n):
        self._nom=n
    @property
    def Adresse(self):
        return self._adresse
    @Adresse.setter
    def Adresse(self,n):
        self._adresse=n
    @property
    def CodePostal(self):
        return self._code
    @CodePostal.setter
    def CodePostal(self,n):
        self._code=n
    @property
    def Ville(self):
        return self._code
    @Ville.setter
    def Ville(self,n):
        self._ville=n
    @property
    def Expedite(self):
        return self._expedite
    @Expedite.setter
    def Expedite(self,n):
        self._expedite=n

    @abstractmethod
    def Prix(Self):
        pass
class Lettre(ObjetPostal):
    def __init__(self, n, adr, cdep, ville, exp,urgence):
        super().__init__(n, adr, cdep, ville, exp)
        self.urg=urgence
    
    def Prix(self):
        prix=0.53
        if self._expedite:
            prix+=1.5
        elif self.urg:
            prix+=0.6
        return prix
class Colis(ObjetPostal):
    def __init__(self, n, adr, cdep, ville, exp,poids):
        super().__init__(n, adr, cdep, ville, exp)
        self.poids=poids
    
    def Prix(self):
        prix=self.poids*0.8/100
        if self._expedite:
            prix+=3
        return prix
if __name__=="__main__":
    saisie = True
    while saisie:
      print("-----Type d'objet------")
      print("1-----Lettre-----")
      print("2-----Colis-----")
      print("3------Quitter-----")
      rep=int(input("Taper votre type d'objet"))
      if rep==1:
            n=input("Taper le nom du destinataire : ")
            adr=input("Taper l'adresse de destinataire : ")
            cde=int(input("Taper le code postal : "))
            vil=input("Taper le nom de ville destination : ")
            exp=bool(int(input("Expedition en recommandé (1=oui/0=non) : ")))
            urg=bool(int(input("Expedition en urgence  (1=oui/0=non) : ")))
            let=Lettre(n,adr,cde,vil,exp,urg)
            
            print(f"le prix à payer est : {let.Prix():.2F}")
      elif rep==2:
            n=input("Taper le nom du destinataire : ")
            adr=input("Taper l'adresse de destinataire :")
            cde=int(input("Taper le code postal : "))
            vil=input("Taper le nom de ville destination : ")
            exp=bool(int(input("Expedition en recommandé (1=oui/0=non) : ")))
            poids=int(input("Taper le poids de votre colis en gramme :"))
            col=Colis(n,adr,cde,vil,exp,poids)
            
            print(f"le prix à payer est : {col.Prix():.2F}")
      elif rep==3:
          print("FIN DE PROGRAMME ")
          saisie=False
      else:
          print("Service introuvable")