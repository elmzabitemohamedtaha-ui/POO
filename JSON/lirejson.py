import json
with open("person.json", "r") as F:
    data = json.load(F)
print(data)
#afficher les loisirs
    
print(F"les loisirs de la personne: {data['loisirs']}")
loisirs=data["loisirs"]
for L in loisirs:
    print(f"-{L}")