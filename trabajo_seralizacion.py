import pickle

lista_nombre=["Juanes","Adrian","Emma","Mark","Jhowan"]

fichero_binario=open("lista_nombre","wb")

pickle.dump(lista_nombre, fichero_binario)


fichero_binario.closed()