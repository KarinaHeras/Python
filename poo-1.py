class Coche():
    def _init_(self):
    self.largoChasis=250
    self.anchoChasis=120
    self.__ruedas=4   # con __con dos guines bajo encapsulamos una varieble
    self.enmarcha=False

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha)
            return"El coche está en marcha"

    def estado(self)  
        if(self.enmarcha):
            return"El coche esta en marcha"  
        else:
            return"el coche esta parado"  
def estado(self):
    print("El coche ", self.__ruedas, "ruedas.un ancho de ", self.anchoChasis, "y un largo de",
     self.largoChasis)

miCoche=Coche()  
print(miCoche.arrancar(True))   

print(miCoche.estado())

print("------A continuacion creamos el seundo objeto-------")

micoche2=coche()
print(micoche2.arrancar(False))
print(miCoche.estado())







