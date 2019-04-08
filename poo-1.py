class Coche():
    def _init_(self): # metodo constructor init con guion bajo uno delante otro despues

        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4            # con __con dos guines bajo encapsulamos una varieble
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.chequeo_interno()

        if(self.__enmarcha and chequeo):
            return"El coche está en marcha"
        elif(self.__enmarcha and chequeo==False):
            return"Algo no va bien en el chequeo"    

        else:
            return"el coche esta parado"  
def estado(self):
    print("El coche ", self.__ruedas, "ruedas.un ancho de ", self.__anchoChasis, "y un largo de",
     self.__largoChasis)


def chequeo_interno(self):
    print("realizando chequeo interno")

    self.gasolina="Ok"
    self.aceite="Ok"
    self.puertas="cerradas"

    if (self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="cerradas"):
        return True
    else:
        return False  

miCoche=Coche()  
print(miCoche.arrancar(True))   

micoche.estado()

print("------A continuacion creamos el seundo objeto-------")

micoche2=Coche()
print(micoche2.arrancar(False))

micoche2.estado()







