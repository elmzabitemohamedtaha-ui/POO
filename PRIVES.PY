class Stagiaire :
    def __init__(self,numero,nom,note):
        self.__numero=numero
        self.__nom=nom
        self.__note=note
    def afficher(self):
        print(f"Numero:{self.__numero}")
        print(f"Nom:{self.__nom}")
        print(f"Note:{self.__note}")
        
if __name__=='__main__':
    stg=Stagiaire(1000,"ali",13.55)
    stg.__numero=2000
    stg.afficher()
    
    
class Stagiaire1:
    def __init__(self,numero,nom,note):
        self.__numero=numero
        self.__nom=nom
        self.__note=note
    #getter pour le numero
    
    def getnumero(self):
        return self.__numero
    #setter pour le numero
    def setnumero(self,newValue):
        self.__numero=newValue
    def getnom(self):
        return self.__nom
    #setter pour le nom
    def setnom(self,newValue):
        self.__nom=newValue
    def getnote(self):
        return self.__note
    #setter pour la note
    def setnote(self,newValue):
        self.__note=newValue
        
    def afficher(self):
        print(f"Numero:{self.__numero}")
        print(f"Nom:{self.__nom}")
        print(f"Note:{self.__note}")
    def __str__(self):
       return f"{self.__numero}\t{self.__nom}\t{self.__note}"
        
if __name__=='__main__':
    stg=Stagiaire1(1000,"ali",13.55)
    #lire la valeur de l'attribut numero
    print(stg.getnumero())
    #modifier la valeur de l'atrribut numero
    stg.setnumero(20)
    print(f"nouveau numero:{stg.getnumero()}")
    print(stg.getnom())
    #modifier la valeur de l'atrribut nom
    stg.setnom("mohamed taha")
    print(f"nouveau nom:{stg.getnom()}")  
    print(stg.getnote())
    #modifier la valeur de l'atrribut note
    stg.setnote(20)
    print(f"nouveau note:{stg.getnote()}")
    print(stg)