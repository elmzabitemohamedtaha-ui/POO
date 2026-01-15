
#valider le format de la date de naissance d'un stagiare
import re
motif=r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
#motifj=r"^[0-9]{1,2}$"
#motifm=r"^[0-9]{1,2}$"
#motifm=r"^[0-9]{4}$"
ve1=input("Taper le jour : ")
#ve2=input("Taper le mois : ")
#ve3=input("Taper l'annnee : ")
rr=re.search(motif,ve1)
#mm=re.search(motifj,ve1)
#aa=re.search(motifj,ve1)
if rr:
    print("Bien")
    print(f"{ve1}")
else:
    print("ressayer")