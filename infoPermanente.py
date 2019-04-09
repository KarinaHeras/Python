import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)

    def __str__(self):
        return "{}{}{}".format(self.nombre, self.genero, self.edad)       

class ListaPersonas:
    persona=[]
    def __init__(self):
        ListaPersonas=open("ficheroExterno", "ab+")
        ListaPersonas.seek(0)

        try:
            self.persona=pickle.load(ListaPersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.persona)))
        except:
            print("El fichero esta vacío")

        finally:
            ListaPersonas.close()
            del(ListaPersonas) 

    def agregarPersonas(self, p):
        self.persona.append(p) 
        self.guardarPersonasEnFicheroExterno()

    def  mostrarPersona(self):
        for p in self.persona:
            print(p) 
            
    def guardarPersonasEnFicheroExterno(self):
        ListaPersonas=open("ficheroExterno", "wb")
        pickle.dump(self.persona, ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)
    def mostrarInfoFicheroExterno(self):
        print(p)

miLista=ListaPersonas()
persona=Persona("Adrian", "Masculino", 3)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno
