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

lista_nombre=["Juanes","Adrian","Emma","Mark","Jhowan"]

fichero_binario=open("lista_nombre","wb")

pickle.dump(lista_nombre, fichero_binario)


fichero_binario.closed()


