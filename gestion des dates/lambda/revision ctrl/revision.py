class Salarie:
    def __init__(self, num, nom, prenom, salaire, tds):
        self._numero=num
        self._nom=nom
        self._prenom=prenom
        self._salaire=salaire
        self._tds=tds
    @property
    def Numero(self):
        return self._numero
    @Numero.setter
    def Numero(self, new):
        self._numero=new
    @property
    def Nom(self):
        return self._nom
    @Nom.setter
    def Nom(self, new):
        self._nom=new
    @property
    def Prenom(self):
        return self._prenom
    @Prenom.setter
    def Prenom(self, new):
        self._prenom=new
    @property
    def Salaire(self):
        return self._salaire
    @Salaire.setter
    def Salaire(self, new):
        self._salaire=new
    @property
    def Tds(self):
        return self._tds
    @Tds.setter
    def Tds(self, new):
        self._tds=new
    def CalculeSalaireNet(self):
        return self._salaire - (self._salaire * self._tds / 100)
    def __eq__(self, other):
        if isinstance(other, Salarie):
            return self._numero == other._numero
        return False
    def __str__(self):
        return f"{self._numero}\t{self._nom} {self._prenom}\t{self._salaire}\t{self._tds}%"
    
class Commercant(Salarie):
    def __init__(self, num, nom, prenom, salaire, tds, chiffre_affaires, tdc):
        super().__init__(num, nom, prenom, salaire, tds)
        self.chiffre_affaires=chiffre_affaires
        self.commission=tdc
    def CalculeSalaireNet(self):
        salairecommission=self.chiffre_affaires*self.commission
        return super().CalculerSalaireNet()+salairecommission
    def __eq__(self, emp):
        return super().__eq__(emp) and self.chiffre_affaires==emp.chiffre_affaires
    def __str__(self):
        return f"{super().__str__()}\t{self.chiffre_affaires}\t{self.commission}%"

if __name__=="__main__":
    s1=Salarie(1,"Taha","Mohammed", 12500, 0.20)
    print(s1)
    print("Le salaire Net est: ")
    print(s1.CalculeSalaireNet())
    c1=Commercant(11, "Rayane", "Lasfar", 12000, 0.20, 30000, 0.10)
    c2=Commercant(11, "Ilyass", "Ennaqui", 11000, 0.20, 30000, 0.10)
    print("Info sur commercant 1: ")
    print(c1)
    print("Info sur commercant 2: ")
    print(c2)
    print(c1==c2)