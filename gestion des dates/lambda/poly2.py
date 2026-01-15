
class Employe:
    def __init__(self, nom,salaire):
        self.nom=nom
        self.salaire=salaire
    def getSalaire(self):
        return self.salaire
    def getSalaire(self,commission=None):
        if commission is None:
            return self.salaire
        return self.salaire+commission
    
    
if __name__=='__main__':
    emp=Employe("ali",8500)
    print("salaire avec comission")
    print(emp.getSalaire(1500))
    print("salaire sans commission:")
    print(emp.getSalaire())