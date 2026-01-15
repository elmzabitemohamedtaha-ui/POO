class Stagiaire:
    
    def __init__(self,numero,nom,note):
        self.numero=numero
        self.nom=nom
        self.note=note
    def decision(self):
        if self.note>=10:
            de="admis"
        elif self.note<=10:
            de="non admis"
        
    
#self.numero represente l'attribut d'instance
#cad la variable associee a l'objet qui existe
#a partir de la creation de l'objet jusqu'a sa destruction 
#la variable numero represente le parametre 
#recu par le constructeur et n'existe que
#dans le corps de ce dernier
    def afficher(self):       
        print(f"{self.numero}\t{self.nom}\t{self.note}")
# question:definir deux objets de type stagiaire et afficher le meilleur stagiaire
'''if __name__=='__main__':'''
stg1=Stagiaire(100,'abdo',12.34)
stg1.afficher()
stg2=Stagiaire(101,'taha',18.34)
stg2.afficher()


if stg1.note>stg2.note:
    print("le stagiaire 1 est le meilleur")
else:
    print("le stagiaire 2 est le meilleur")