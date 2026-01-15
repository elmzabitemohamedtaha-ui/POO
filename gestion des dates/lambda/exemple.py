from datetime import datetime
class Stagiaire:
    def __init__(self,code,nom,dns,note):
        self.__code=code
        self.__nom=nom
        self.__dns=datetime.strptime(dns,"%d/%m/%Y")
        self.__note=note
        
    @property 
    def Code(self):
        return self.__code
    @Code.setter
    def Code(self,C):
        self.__code=C
    @property 
    def Nom(self):
        return self.__nom
    @Nom.setter
    def Nom(self,N):
        self.__nom=N
    @property 
    def Dns(self):
        return self.__dns
    @Dns.setter
    def Dns(self,d):
        self.__dns=d
    @property 
    def Note(self):
        return self.__note
    @Note.setter
    def Note(self,n):
        self.__note=n
    def __str__(self):
        return f"{self.__code}\t{self.__nom}\t{self.__dns.date()}\t{self.__note}"
if __name__=='__main__':
    maliste=[]
    stg1=Stagiaire(1,"taha","20/03/2008",19)
    stg2=Stagiaire(2,"mohamed","21/02/2008",19.5)
    stg3=Stagiaire(3,"ilyas","20/03/2008",20)
    stg4=Stagiaire(4,"anas","20/05/2008",18)
    maliste.append(stg1); maliste.append(stg2); maliste.append(stg3); maliste.append(stg4)
    maliste.sort(key=lambda m:m.Dns)
    for m in maliste:
        print(m)
    
        
        
        
        
        
        