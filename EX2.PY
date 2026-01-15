class Client:
    def __init__(self,n:str,p:str,v:str):
        self.__nom=n
        self.__prenom=p
        self.__ville=v
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,n):
        self.__nom=n
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self,p):
        self.__prenom=p
    @property
    def ville(self):
        return self.__ville
    @ville.setter
    def ville(self,v):
        self.__ville=v
        
        
        
    
        
class Compte:
    
    def __init__(self,numero,c,solde):
        self.__numero=numero
        self.__Client=c
        self.__solde=solde
    
    def setdepot(self,newValue):
        self.__solde=newValue
    def getdepot(self):
        return self.__solde
    def settitiulaire(self,newValue):
        self.__titulaire=newValue
    def gettitulaire(self):
        return self.__titulaire
    def setsolde(self,newValue):
        self.__solde=newValue
    def getsolde(self):
        return self.__solde
    def deposer(self,m):
        self.__solde+=m
    def retirer(self,m):
        if m>self.__solde:
            print("solde insuffisant")
        else:
            self.__solde-=m
            
    def __str__(self):
        return f"{self.__numero}\t{self.__Client.nom}\t{self.__Client}\t{self.__Client.prenom}\t{self.__solde}\t"
C1=Client("taha","mohamed","casablanca") 
C2=Client("mohamed","taha","casablanca")
 
compt1=Compte(1000,C2,2000000000000000000000000)
print(compt1)
print("depot de 10000")
compt1.deposer(10000)
print(compt1)
print("retrait de 5000")
compt1.retirer(5000)
print(compt1)