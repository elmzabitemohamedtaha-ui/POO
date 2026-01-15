class Livre:
    def __init__(self,titre,nom,prix):
        self.nom=nom
        self.titre=titre
        self.prix=prix
    def afficher(self):
        print(F"LE LIVRE{self.nom} ECRIT PAR {self.titre} NE VEND A {self.prix} EUROS")
if __name__=='__main__' :
    lvr=Livre("pascal masson","100 exercices python pour s'entrainer",10.99)
    lvr.afficher()