#exemple2
#l'utilisateur doit saisir 
import re
motif=r"^[0-9]$" #motif=r"\d"
#exemple de chaine
ch=input("taper un chiffre :")
verifier=re.search(motif,ch)
if verifier :
    print("saisie valide")
else:
    print("saisie n'est pas valide")
#remarque si on saisie par exemple 78
#la saisie est valide