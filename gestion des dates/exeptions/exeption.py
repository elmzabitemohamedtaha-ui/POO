#chaque classe d'exception personnalitee herite de la classe exception 
#etape1:
class AgeError(Exception):
    def __init__(self):
        super().__init__("l'age doit etre positif")
#etape2:
#indiquer la ou l'exception doit etre levee en utilisant le mot-cle raise
class Personne:
    def __init__(self,num,n,a):
        self.nom=num
        self.prenom=n
        if a<0:
            raise AgeError()
        self.age=a
    def __str__(self) -> str:
        return f"Nom: {self.nom}\t {self.prenom} \t{self.age} "
'''if __name__ == '__main__':
    pers=Personne("mohamed","taha",30)
    print(pers)'''
#etape 3: il faut gerer l'exeption a l'aide de try...except
if __name__=='__main__':
    try:
        num=int(input("taper le numero :"))
        nom=input("taper le nom:")
        a=int(input("taper l'age:"))
        pers=Personne(num,nom,a)
        print(pers)
    except AgeError as e:
        print(f"Erreur: {e}")



