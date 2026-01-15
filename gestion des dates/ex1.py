class Chauffeur:
    def __init__(self,cin,nom,prenom):
        self.cin = cin
        self.nom = nom
        self.prenom = prenom
    @property
    def Cin(self):
        return self.cin
    @Cin.setter
    def Cin(self,new):
        self.cin=new
    @property
    def Nom(self):
        return self.Nom
    @Nom.setter
    def Nom(self,new):
        self.nom=new
    @property
    def Prenom(self):
        return self.prenom
    @Prenom.setter
    def Prenom(self,new):
        self.prenom=new
    def __str__(self):
        return f"{self.cin}/t{self.nom}/t{self.prenom}"
    
        
    