#verifier que tous les lettres d'une chaine sont au muniscules 
import re
motif=r"^[a-z]+$"
#exemple de chaine
ch=input("taper  :")
verifier=re.search(motif,ch)
if verifier :
    print("saisie valide")
else:
    print("saisie n'est pas valide")