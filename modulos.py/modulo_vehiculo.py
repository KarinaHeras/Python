class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arranca(self):
        self.enmarcha=True  

    def acelera(self):
        self.acelera=True

    def frena(self):
        self.frena=True 
    def estado(self):
         print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena, "\n", self.hcaballito)    

class Furgoneta(Vehiculos):        
    def carga(self, cargada):
        self.carganda=cargar
        if (self.cargada)
            return"La furgoneta esta cargada"
        else:
            return"La furgoneta no esta cargada"

class VElectricos():
    def _init_(self):
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True

    
class Moto(Vehiculos):
    hcaballito=""
def caballito(self):
  self.hcaballito="Voy haciendo caballito"



                   
        