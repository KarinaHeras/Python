class Coche():
    def deplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
     def deplazamiento(self):
       print("Me desplazo utilizando dos ruedas")  

class Camion():
     def deplazamiento(self):
     print("Me desplazo utilizando seis ruedas")    


def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo=Camion()   

desplazamientoVehiculo(miVehiculo)