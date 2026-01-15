import math
class Point:
    def __init__(self,x=None,y=None):
        self.__abscisse=x
        self.__ordonnees=y
    def getabscisse(self):
        return self.__abscisse
    
    def setabscisse(self,newValue):
        self.__abscisse=newValue
    def getordonnees(self):
        return self.__ordonnees
    
    def setordonnees(self,newValue):
        self.__ordonnees=newValue
        
    def distance(self):
        return math.sqrt(self.__abscisse**2+self.__ordonnees**2)
    def __str__(self):
        return f"{self.distance()}\t{self.__abscisse}\t{self.__ordonnees}"
    
if __name__=='__main__':
    A=Point()
    A.setabscisse=12
    A.setordonnees=10
    
    B=Point()
    B.setabscisse=4
    B.setordonnees=3
    print(B)
    A=B
    print(A)
    
    

    
            
        
    