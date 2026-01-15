class Personne:
    def __init__(self,nom):
        self.nom=nom
    def Afficher(self):
        print("je suis une personne")
class Stagiaire(Personne):
    def __init__(self, nom,f):
        super().__init__(nom)
        self.filiere=f
    def Afficher(self):
        print("je suis un stagiaire")
class Employe(Personne):
    def __init__(self, nom,salaire):
        super().__init__(nom)
        self.salaire=salaire
    def Afficher(self):
        print("je sui un employe")
if __name__=='__main__':
    p=Personne("ali") 
    stg=Stagiaire("chouaib","dev")
    emp=Employe("nadia",8900)      
    maliste=[]
    maliste.append(p);maliste.append(stg)
    maliste.append(emp)
    for  m in maliste:
        m.Afficher()
