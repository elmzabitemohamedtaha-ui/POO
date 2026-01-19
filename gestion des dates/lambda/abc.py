from abc import abstractmethod
#interface comparable en python
class Comparable:
    @abstractmethod
    def compareTo(self):
        pass
#la classe personne implimente l'interface comparable
class Personne(Comparable):
    def __init__(self,n,a):
        self.__nom=n
        self.__age=a
    def compareTo(self,p):
        if isinstance(p,Personne):
            return self.__age==p.__age
        return False
class Outils(Comparable):
    def __init__(self,prix,long):
        self.__prix=prix
        self.__longueur=long,
    def compareTo(self,o):
        if isinstance(o,Outils):
            return self.__longueur==o.__longueur
        return False
if __name__=='__main__':
    p1=Personne("nom1",22)
    p2=Personne("nom2",23)
    if p1.compareTo(p2):
        print("les deux personnes ont le meme age")
    else:
        print("les deux pesonnes n'ont pas le meme age")
        
    
    
        
        
    