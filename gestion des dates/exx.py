class Article:
    def __init__(self, numero_serie=None, prix_ht=None, quantite_stock=None, quantite_minimale=None):
        self.numero_serie = numero_serie
        self.prix_ht = prix_ht
        self.quantite_stock = quantite_stock
        self.quantite_minimale = quantite_minimale
    def __str__(self):
        return (f"Article - Série: {self.numero_serie}, Prix HT: {self.prix_ht} DH, "
                f"Stock: {self.quantite_stock}, Min Stock: {self.quantite_minimale}")
    def s_approvisionner(self, qte):
        self.quantite_stock += qte
        print(f"Stock mis à jour. Nouveau stock: {self.quantite_stock}")

    def achat(self, qte):
        if self.quantite_stock >= qte:
            self.quantite_stock -= qte
            print(f"Achat effectué. Stock restant: {self.quantite_stock}")
            if self.quantite_stock < self.quantite_minimale:
                print("Avis: La quantité en stock est inférieure à la quantité minimale.")
        else:
            print("Erreur: Quantité demandée supérieure au stock disponible.")
class Habit(Article):
    def __init__(self, numero_serie=None, prix_ht=None, quantite_stock=None, quantite_minimale=None, taille=None, couleur=None):
        super().__init__(numero_serie, prix_ht, quantite_stock, quantite_minimale)
        self.taille = taille
        self.couleur = couleur
    def __str__(self):
        return (f"Habit - Série: {self.numero_serie}, Prix HT: {self.prix_ht} DH, "
                f"Stock: {self.quantite_stock}, Min Stock: {self.quantite_minimale}, "
                f"Taille: {self.taille}, Couleur: {self.couleur}")
from datetime import date, timedelta

class Electromenager(Article):
    def __init__(self, numero_serie=None, prix_ht=None, quantite_stock=None, quantite_minimale=None, poids=None, duree_garantie_mois=None):
        super().__init__(numero_serie, prix_ht, quantite_stock, quantite_minimale)
        self.poids = poids
        self.duree_garantie_mois = duree_garantie_mois
    def datefinGarantie(self):
        jours_garantie = self.duree_garantie_mois * (365.25 / 12) # Approximation
        date_fin = date.today() + timedelta(days=jours_garantie)
        return date_fin.strftime("%d/%m/%Y")
    def __str__(self):
        return (f"Electromenager - Série: {self.numero_serie}, Prix HT: {self.prix_ht} DH, "
                f"Stock: {self.quantite_stock}, Min Stock: {self.quantite_minimale}, "
                f"Poids: {self.poids} kg, Garantie: {self.duree_garantie_mois} mois, "
                f"Date fin garantie: {self.datefinGarantie()}")
if __name__ == '__main__':
    mon_habit = Habit("H123", 150.00, 10, 5, "M", "Bleu")
    mon_habit.s_approvisionner(20)
    print(mon_habit)
    mon_electromenager = Electromenager("E456", 1200.00, 5, 2, 8.5, 24)
    mon_electromenager.achat(2)
    print(f"La date de fin de garantie est : {mon_electromenager.datefinGarantie()}")
    print(mon_electromenager)
    
    