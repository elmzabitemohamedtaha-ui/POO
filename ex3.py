class Salarie:
    def __init__(self,matricule,nom,prenom,salaire,taux):
        self.__matricule=matricule
        self.__nom=nom
        self.__prenom=prenom
        self.__salaire=salaire
        self.__taux=taux
    def calculerSalaireNet(self):
        return self.__salaire-(self.__salaire*self.__taux)
    def setmatricule(self,newValue):
        self.__matricule=newValue
    def getmatricule(self):
        return self.__matricule
    def setnom(self,newValue):
        self.__nom=newValue
    def getnom(self):
        return self.__nom
    def setprenom(self,newValue):
        self.__prenom=newValue
    def getprenom(self):
        return self.__prenom
    def setsalaire(self,newValue):
        self.__salaire=newValue
    def getsalaire(self):
        return self.__salaire
    def set(self,newValue):
        self.__taux=newValue
    def gettaux(self):
        return self.__taux
    def __str__(self):
        return f"{self.__matricule}\t{self.__nom}\t{self.__prenom}\t{self.__salaire}\t{self.__taux}\t{salarie1.calculerSalaireNet}"
    
salarie1=Salarie(12,"MOHAMED","TAHA",5000,0.25)

salarie2=Salarie(13,"MOHAMED","TAHA",10000,0.25)
print(salarie1)
print(salarie2)