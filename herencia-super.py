class Persona():
    def _init_(self, nombre, edad, Lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.Lugar_residencia=Lugar_residencia

def descripcion(self):
    print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

class Empleado():
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado ):
         super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
         self,salario=salario
         self.antigüedad=antigüedad

    def descripcion(self):
        super().descripcion()

          print("Salario: ", self.salario, "Antigüedad: ",  self.antigüedad) 

Juanes=Empleado("Juanes", 15, "Colombia")        
Juanes.descripcion()

print(isinstance(Juanes, Persona))