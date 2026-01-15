#exemple3
#l'utilisateur doit saisir exactement deux chiffres 
import re
motif=r"^[0-9]{2}$ "
#exemple de chaine
ch=input("taper un chiffre :")
verifier=re.search(motif,ch)
if verifier :
    print("saisie valide")
else:
    print("saisie n'est pas valide")