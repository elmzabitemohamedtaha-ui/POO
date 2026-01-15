class Bus:
    def __init__(self,immatriculation,marque,type):
        self.immatriculation =immatriculation 
        self.marque = marque
        self.type = type
    @property
    def Immatriculation(self):
        return self.immatriculation
    @Immatriculation.setter
    def Immatriculation(self,new):
        self.immatriculation=new

    @property
    def Marque(self):
        return self.marque
    @Marque.setter
    def Marque(self,new):
        self.marque=new

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self,new):
        self.type=new
    def __str__(self):
        return f"{self.immatriculation}\t{self.marque}\t{self.type}"
if __name__=='__main__':
    bus1=Bus("34-567-89","mercedes","tourisme")
    print(bus1)
    bus2=Bus("12-345-67","audi","transport")
    print(bus2)



    
        
    