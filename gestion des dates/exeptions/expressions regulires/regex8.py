#Valider l'email d'un utilisateur
import re
motif=r"^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]{2,}$"
'''motif=r"^[^\s@]+@[^\s@]+\.[^\s@]+$" '''#deuxieme methode:compter le nombre d'espace
ver=input("Taper le gmail :")
r=re.search(motif,ver)
if r:
    print(" verifier")
else:
    print(" n'est pas validée")