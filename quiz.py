import json
with open("quiz.json", "r") as F:
    data = json.load(F)
#le nombre des questions proposées
n=len(data)

#un compteur de reponses exactes
compt=0
for d in data:
    rep=input(d["question"])
    if rep==d["reponse"]:
        compt+=1
print(f"votre score est {compt} / {n}")
