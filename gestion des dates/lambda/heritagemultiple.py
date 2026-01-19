class Personne:
    def __init__(self,n,p):
        self._nom=n
        self._prenom=p
    def __str__(self):
        return f"{self._nom} {self._prenom}"
class InfoSupp:
    def __init__(self,adr,em):
        self._adresse=adr
        self._email=em
    def __str__(self):
        return f"{self._adresse} {self._email}"
class Etudiant(Personne,InfoSupp):
    def __init__(self, n, p,adr,em,f):
        #appel du constructeur d'initialisation de la clss mere Personne
        Personne.__init__(self,n,p) #self obligatoire
        #appel du constructeur d'initialisation de la classe mere InfoSupp
        InfoSupp.__init__(self,adr,em) #self obligatoire
        self.filiere=f
    def __str__(self):
        return Personne.__str__(self)+InfoSupp.__str__(self)        
      
        
        