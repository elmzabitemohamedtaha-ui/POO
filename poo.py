#POUR DECLARER UNE CLASSE EN PYTHON
#ON UTILISE LE MOT-CLE CLASS
class MaClasse:
    pass

#pour creer un instance de la classe
#MaClasse:
obj=MaClasse()

#exemple d'une attribut
class stagiaire:
    nom="ahmed" #attribut nom
    age=20 #attribut age
    def afficher(self):
        print(f"nom est:{self.nom}")
        print(f"age est:{self.age}")
    
    
#creation d'un objet de type stagiaire
stg=stagiaire()
stg.afficher()