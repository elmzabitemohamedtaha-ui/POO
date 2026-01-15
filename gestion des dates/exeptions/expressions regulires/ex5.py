#la premiere lettre en MAJ et le reste
#des lettres en miniscules
import re
motif=r"^[A-Z][a-z]$" #motif=r"\d"
#exemple de chaine
ch=input("taper :")
verifier=re.search(motif,ch)
if verifier :
    print("saisie valide")
else:
    print("saisie n'est pas valide")