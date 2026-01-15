#le numero du stagiaire doit etre 
#le premier objet aura le numero:1
#le deuxieme objet aura le numero:2
#et aussi
class Stagiaire:
    compteur=1
    def __init__(self,num=None,n=None,a=None):
        
        self.__numero=num
        self.__nom=n
        self.__age=a
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self,num):
        self.__numero=num
    @property
    def nom(self):
        return self.__nom
    @numero.setter
    def nom(self,n):
        self.__nom=n
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,a):
        self.__age=a
    def __str__(self) -> str:
        f"{self.__numero}\t{self.__nom}\t{self.__age}"

if __name__=='__main__':
    stg1=Stagiaire('ali',21)
    print(stg1)
    stg2=Stagiaire()
    stg2.nom='mohamed'
    stg2.age=22
    print(stg2)
        
        


        
        
    
    