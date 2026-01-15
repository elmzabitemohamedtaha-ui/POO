#verifier q'une chaine comporte un caractere majuscule
import re
motif=r"[A-Z]"
#exemple de chaine
ch="deveLoppement"
'''verifier=re.search(motif,ch)
if verifier:
    print("chaine validee")
else:
    print("chaine non validee")'''
#la fonction findall() trouve toutes les correspondences d'un motif dans une chaine 
verif=re.findall(motif,ch)
print(verif)
