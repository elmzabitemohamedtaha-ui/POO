class Cercle:
    def __init__(self,r,x,y):
       self.rayon=r
       self.abscisse=x
       self.ordonnee=y
       
    def surface(self):
        return 3.14*self.rayon**2
    def perimetre(self):
        return 2*3.14*self.rayon*2
    def afficher(self):
        print(f"le cercle de rayon: {self.rayon} et la position de son centre est  {self.abscisse},{self.ordonnee}")
        print(f"la surface est :{self.surface():.2F}")
        print(f"le perimetre est:{self.perimetre():.2F}")
ra=float(input(f"taper le rayon:"))
xe=float(input(f"taper l'abscisese du centre:"))
ye=float(input(f"taper l'ordonnee du centre:"))
cer1=Cercle(ra,xe,ye)
cer1.afficher()