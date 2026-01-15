import json
#creer un dictionnaire
data={
    "code":1000,
    "nomcomplet":"NENNIS MARIAM",
    "specialite":"gestion",
    "noteExam":15.75,
    "loisirs":["lecture","sport","voyage"]
    
}
#convertir data en fichier format JSON
with open("stagiaire.json","w") as F:
    json.dump(data,F)
print("sauvegarde ave succes")