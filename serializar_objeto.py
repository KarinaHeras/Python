import pickle

class Vehiculos():
    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

        def arrancar(self):
             self.enmarcha=True  

        def acelera(self):
             self.acelera=True

        def frena(self):
             self.frena=True

    def estado(self):
         print("marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
            self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",self.frena)    

coche1=Vehiculos("Mazda", "MX5")
coche2=Vehiculos("SEAT", "leon")
coche3=Vehiculos("Renault", "Megane")

coche=[coche1,coche2,coche3]

fichero=open("loscoches", "wb")

pickle.dump(coche,fichero)

fichero.close()

del (fichero)

ficheroApertura=open("loscoches","rb")

misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
    print(c.estado())

                   
        