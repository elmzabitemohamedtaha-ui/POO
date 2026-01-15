class Personne:
    def __init__(self,num,n,age):
        self.__numero=num
        self.__nom=n
        self.Age=age
    @property
    def Numero(self):
        return self.__numero
    @Numero.setter
    def Numero(self,new):
        self.__numero=new
    @property
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,new):
        self.__nom=new
    @property
    def Age(self):
        return self.__age
    @Age.setter
    def Age(self,new):
        if new<0:
            raise ErreurAge()
        self.__age=new
    def __str__(self) -> str:
        return f"{self.__numero}\t {self.__nom} \t{self.__age} "
class ErreurAge(Exception):
    def __init__(self):
        super().__init__()
    def Getmessage(self):
        return "l'age doit etre positif"
if __name__=='__main__':
    try:
        p=Personne(1,"taha",-17)
    except ErreurAge as e:
        print(f"Erreur : {e.Getmessage()}")