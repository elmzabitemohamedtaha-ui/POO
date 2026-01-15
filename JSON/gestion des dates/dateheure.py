from datetime import datetime ,date,timedelta
d1=datetime.today()
#pour afficher la date complet avec l'horaire jour+heure
print(d1)
d2=date.today()
#pour afficher juste la date du joure
print(d2)
#pour extraire le jour , mois , annee
j=d2.day
print(f"Jour : {j} ")
m=d2.month
print(f"le mois est : {m} ")
y=d2.year
print(f"l'annee est : {y} ")
#pour afficher les heures seulement
h=d1.hour#ici d2 doesn't work car d2 contient seulement la date du jour
print(f"le nombre d'heure est : {h} ")
#pour afficher les minutes seulement
min=d1.minute
print(f"minutes : {min}")
#pour afficher les secondes seulement
sec=d1.second
print(f"secondes : {sec}")
#en utilisant les formats 
print(f"le jour est : {d1:%d}")
print(f"le mois est : {d1:%B}")
print(f"l'annee est : {d1:%Y}")
#comparaison entre deux dates
j1=int(input("taper le jour du premiere date:"))
m1=int(input("taper le mois du premiere date:"))
a1=int(input("taper l'annee du premiere date:"))
d1=date(a1,m1,j1)
j2=int(input("taper le jour du deuxieme date:"))
m2=int(input("taper le mois du deuxieme date:"))
a2=int(input("taper l'annee du deuxieme date:"))
d2=date(a2,m2,j2)
if d1>d2:
    print("la premiere date est superieur a la seconde")
else:
    print("la premiere date est inferieur a la seconde")
    
#pour ajouter un intervalle sur le temps on importe timedelta
d1=date.today()
delta=timedelta(days=10)
print(f"dans dix jours,la date sera :{d1+delta}")
print(f"dans dix jours,la date etait :{d1-delta}")




