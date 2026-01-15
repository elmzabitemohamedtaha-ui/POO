class Voyage:
    _compteur_voyages = 1

    def __init__(self, vchauffeur, vbus, date_voyage):
        self.__numero_voyage = Voyage._compteur_voyages
        Voyage._compteur_voyages += 1
        self.__vchauffeur = vchauffeur
        self.__vbus = vbus
        self.__date_voyage = date_voyage
    @property
    def Vchauffer(self):
        return self.__vchauffeur
    @Vchauffer.setter
    def Vchauffer(self,new):
        self.__vchauffeur=new
    @property
    def Vbus(self):
        return self.__vbus
    @Vbus.setter
    def Vbus(self,new):
        self.__vbus=new
    @property
    def Date_voyage(self):
        return self.__date_voyage
    @Date_voyage.setter
    def Date_voyage(self,new):
        self.__date_voyage=new
    def __str__(self):
        return f"Voyage numero : {self.__numero_voyage} \t Chauffeur : {self.__vchauffeur}\t Bus : {self.__vbus}\t Date du voyage : {self.__date_voyage}"
    def recette(self, nombre_voyageurs, prix_billet):
        return nombre_voyageurs * prix_billet


if __name__ == "__main__":
    v = Voyage("mohamed", "Bus", "2025-12-19")
    nombre = 30
    prix = 200.0
    print(v)
    print("Recette du voyage =", v.recette(nombre, prix))


