from datetime import datetime,date
class Stagiaire:
    def __init__(self,numero,nom,dns):
        self.numero=numero
        self.nom=nom
        self.dns=datetime.strptime(dns,"%d/%m/%Y")
    def getage(self):
        d=date.today()
        age=d.year-self.dns.year
        if d.month<self.dns.month or d.month==self.dns.month and d.day<self.dns :
            age=age-1
        return age
    def __str__(self):
        return f"{self.numero}\t{self.nom}\t{self.dns.date()}\t{self.getage()}"
if __name__=='__main__':
    s=Stagiaire(1,"mohamed taha","20/03/2008")
    print(s)

        
    
        