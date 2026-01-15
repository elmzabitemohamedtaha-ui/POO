class Salairie:
    def __init__(self,num,nom,prenom,salaire ,tauxcharge):
        self._numero=num
        self._nom=nom
        self._prenom=prenom
        self._salaire=salaire
        self._tauxcharge=tauxcharge
    @property
    def Numero(self):
        return self._numero
    @Numero.setter
    def Numero(self,new):
        self._numero=new
    
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
    def Salaire(self):
        return self._salaire
    @Salaire.setter
    def Salaire(self,new):
        self._salaire=new
    @property
    def Taux_charges (self):
        return self._tauxcharge
    @Taux_charges.setter
    def Taux_charges(self,new):
        self._tauxcharge=new
    def CalculeSalaireNet(self):
        return self._salaire - (self._salaire * self._tauxcharge/100)
    def __eq__(self, value):
        return self._numero==value._numero
    def __str__(self):
        return f"{self._numero}:\t{self._nom}\t{self._prenom}\t{self._salaire}\t{self._tauxcharge}%\t{self.CalculeSalaireNet()}"
class Commercant(Salairie):
    def __init__(self, num, nom, prenom, salaire, tauxcharge,chfraffaire,taux):
        super().__init__(num, nom, prenom, salaire, tauxcharge)
        self.chfraffaire=chfraffaire
        self.taux=taux
    def SalaireCommercant(self):
        salaire_bas=super().CalculeSalaireNet()
        comission = self.chfraffaire*self.taux/100
        return salaire_bas + comission
    def __eq__(self, value):
        return super().__eq__(value) and self.chfraffaire==value.chfraffaire
    def __str__(self):
        return f"{super().__str__()}\t{self.chfraffaire}\t{self.taux}\t{self.SalaireCommercant()}"
if __name__=='__main__':
    s=Salairie (1,"mohamed","taha",20000,10)
    print(s)
    c=Commercant (2,"amine","yassine",30000,15,50000,5)
    print(c)
    print(s==c)
    