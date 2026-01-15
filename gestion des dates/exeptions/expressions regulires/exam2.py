import re
import json
class Stagiaire:
  def __init__(self, num, nom):
    
    motif=r"^[0-9]{12}+$"
    verif=re.search(motif,str(num))

    if verif:
      self.__numero=str(num)
      self.__nom=nom
    else:
      raise Exception("le numero doit etre compose de 12 chiffres")
  @property
  def Numero(self):
    return self.__numero
  @Numero.setter
  def Numero(self, new):
    self.__numero=str(new)
  @property
  def Nom(self):
    return self.__nom
  @Nom.setter
  def Nom(self, new):
    self.__nom=new
  def toDict(self):
       mondict={
           "numero":self.__numero,
           "nom":self.__nom,
       }
       return mondict
  def __eq__(self, stg):
    if isinstance(stg, Stagiaire):
      return self.__numero == stg.__numero
    return False
  def __str__(self):
    return f"Stagiaire {self.__numero}: {self.__nom}"

class Club:
  def __init__(self, nomclub):
    self.__nomclub=nomclub
    self.Lmembres=[]
  @property
  def NomClub(self):
    return self.__nomclub
  @NomClub.setter
  def NomClub(self, new):
    self.__nomclub=new
  @property
  def NombreMembres(self):
    return len(self.Lmembres)
  def IndiceDe(self, membre):
    if membre in self.Lmembers:
      return self.Lmembers.index(membre)
    else:
      return -1
  def ajouter(self, membre):
    if membre not in self.Lmembres:
      self.Lmembres.append(membre)
      return True
    else:
      return False
  def afficher(self):
    print(f"Nom du club: {self.NomClub}")
    print(f"Le nombre des membres est: {self.NombreMembres}")
    for s in self.Lmembres:
      print(s)
  def supprimer(self, p):
    if isinstance(p, Stagiaire):
      if p in self.Lmembres:
        self.Lmembres.remove(p)
      else:
        raise Exception("Membre introuvable")
    elif isinstance(str(p), str):
      trouver=False
      for s in self.Lmembres:
        if s.Numero==str(p):
          self.Lmembres.remove(s)
          print("Suppression avec succes !")
          trouver=True
          break
      if trouver==False:
        raise Exception("Numero introuvable")
      
  def enregistrer(self):
        newListe=[]
        for stg in self.Lmembres:
            newListe.append(stg.toDict())
        with open("Club.json","w") as F:
            json.dump(newListe,F)
        print("Sauvegarde avec succes")
  def charger(self):
      with open ("club.json","r") as f:
         data=json.load(f)
      for d in data:
          print(f"{d['numero']}\t{d['nom']}")


if __name__=='__main__':
  s1=Stagiaire(199611050035, "Hassan SOUFIANI")
  s2=Stagiaire(199609150002, "Imane BARKAOUI")
  s3=Stagiaire(199501050112, "Aissam ALAOUI")
  s4=Stagiaire(199802130190, "Badr MOUBTASSIM")
  c=Club("Jeux d'Echecs")
  c.ajouter(s1);c.ajouter(s2);c.ajouter(s3);c.ajouter(s4)
  c.enregistrer()
  c.afficher()
  c.supprimer(s1)
  c.afficher()
  c.supprimer(199609150002)
  c.afficher()
  c.charger()