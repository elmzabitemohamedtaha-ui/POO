from datetime import datetime,date,timedelta
class Joueur:
    def __init__(self,nom,age,position,experimenté):
        self._nom=nom
        self._age=age
        self._position=position
        self._experience=experimenté
#Les accesseurs
    @property
    def Nom(self):
        return self._nom
    
    @property
    def Age(self):
        return self._age
    
    @property
    def Position(self):
        return self._position
    
    @property
    def Experience(self):
        return self._experience
    
    def CalculerPrime(self,interne,externe):
        prime=20000*interne+30000*externe
        if self._experience:
            prime += prime*0.5
        return prime 
#la classe internationale hérite de la classe joueur
class Internationale(Joueur):
    def __init__(self, nom, age, position, experimenté,cumulannee):
        super().__init__(nom,age,position,experimenté)
    #Exception pour que le cumule d'année doit etre inferieure a l'age du joueur
        if age < cumulannee:
            raise Exception("Le cumule d'année doit etre inferieure a l'age du joueur")
        self.cumulannee=cumulannee

    def CalculerPrime(self, interne, externe):
        return super().CalculerPrime(interne, externe)+5000*self.cumulannee
class Entraineur:
    def __init__(self,nom,datefin,nbannee,primeannuelle):
        self.nom=nom
        self.datefin=datetime.strptime(datefin,"%d/%m/%Y")
        self.nbannee=nbannee
        if primeannuelle<3000 and primeannuelle>6000:
            raise Exception ("la prime annuelle doit etre entre 3000MAD et 6000MAD ")
        self.primeannulle=primeannuelle

    def DeterminerDebutContrat(self):
        periode=self.nbannee*365
        debut=self.datefin-timedelta(days=periode)
        return debut.strftime("%d/%m/%Y")
    
class Section():
    def __init__(self,pays,surnom,nmi,nme,entraineur):
        self.pays=pays
        self.surnom=surnom
        self.nbmatchinterne=nmi
        self.nbmatchexterne=nme
        self.entraineur=entraineur
        self.Ljrs=[]

    @property
    def Ljrs(self):
        return self.Ljrs

if __name__=="__main__":
    ent1=Entraineur("Adam","12/3/2030",10,4000)
    print(ent1.DeterminerDebutContrat())