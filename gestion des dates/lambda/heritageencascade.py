class Personne:
    def __init__(self,m,n,p):
        self._matricule=m
        self._nom=n
        self._prenom=p
    def __str__(self):
        return f"{self._matricule} {self._nom} {self._prenom}"
class Etudiant(Personne):
    def __init__(self,m,n,p,f):
        super().__init__(m,n,p)
        self._filiere=f
        
    def __str__(self):
        return super().__str__()+" "+f"{self._filiere}"
class Etudiant_2A(Etudiant):
    def __init__(self, m, n, p, f,o):
        super().__init__(m, n, p, f)
        self.option=o

    def __str__(self):
        return super.__str__(self)+" "+f"{self.option}"   
#programme de test:
et=Etudiant_2A(100,"alami","rachid","TSDD","full stack")
      
        
        