class Salarié:
    def __init__(self,num,nom,prenom,salaire,taux):
        self._numero=num
        self._nom=nom
        self._prenom=prenom
        self._salaire=salaire
        self._taux=taux
    #Accesseurs et mutateurs
    @property
    def Numero(self):
        return self._numero
    @Numero.setter
    def Numero(self,new):
        self._numero=new

    @property
    def Nom(self):
        return self._nom
    @Numero.setter
    def Numero(self,new):
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
    def Taux(self):
        return self._taux
    @Taux.setter
    def Taux(self,new):
        self._taux=new

    def CalculerSalaireNet(self):
        return self._salaire-(self._salaire*self._taux)
    
    def __eq__(self,emp):
        if isinstance(emp,Salarié):
            return self._numero==emp._numero
        return False
    def __str__(self):
        return f"{self._numero}\t {self._nom}\t {self._prenom}\t {self._salaire}\t {self._taux}"
    
class Commerçant(Salarié):
    def __init__(self, num, nom, prenom, salaire, taux,chaffaire,tauxcomission):
        super().__init__(num, nom, prenom, salaire, taux)
        self.chiffre=chaffaire
        self.comission=tauxcomission

    def CalculerSalaireNet(self):
        salairecomission=self.chiffre*self.comission
        return super().CalculerSalaireNet()+salairecomission
    def __eq__(self, emp):
        return super().__eq__(emp) and self.chiffre==emp.chiffre
    def __str__(self):
        return super().__str__()+f"\t{self.chiffre}\t {self.comission}"

if __name__=="__main__":
    sal1=Salarié(10,"Rayane","Lasfar",12000,0.20)
    print(sal1)
    print("Le salaire net est")
    print(sal1.CalculerSalaireNet())
    com1=Commerçant(11,"Adam","Elbahja",11000,0.20,14000,0.10)
    com2=Commerçant(12,"Mohammed","Mouhim",15000,0.20,14000,0.10)
    print("Info sur commerçant 1 :")
    print(com1)
    print("Info sur commerçant 2:")
    print(com2)
    print(com1==com2)