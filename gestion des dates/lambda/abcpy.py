import math
from abc import ABC, abstractmethod
class Forme(ABC):
    def __init__(self,n):
        self._nom=n
    #methodes abstraites
    @abstractmethod
    def CalculerPerimetre(self):
        pass
    @abstractmethod
    def CalculerSurface(self):
        pass
    def __str__(self) -> str:
        return f" {self._nom}"
class Rectangle(Forme):
    def __init__(self, n,Long,larg):
        super().__init__(n)
        self._longueur=Long
        self._largeur=larg
    
    def CalculerPerimetre(self):
        return (self._longueur + self._largeur)*2
    def CalculerSurface(self):
        return self._longueur * self._largeur
    def __str__(self) -> str:
        a = super().__str__()
        a+=f"\t{self._longueur}\t{self._largeur}"
        return a
class Cercle(Forme):
    def __init__(self,n,R):
        super().__init__(n)
        self._rayon=R
    def CalculerPerimetre(self):
        return 2*math.pi*self._rayon
    def CalculerSurface(self):
        return math.pi*(self._rayon**2)
    def __str__(self) -> str:
        return super().__str__()+f"\t{self._rayon}"

    
if __name__=="__main__":
    rect=Rectangle("rectangle",5,3)
    print(rect)
    print(f"Perimetre: {rect.CalculerPerimetre()}")
    print(f"Surface: {rect.CalculerSurface()}")

    
      