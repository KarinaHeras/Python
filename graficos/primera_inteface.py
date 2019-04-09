from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")
raiz.resizable(True,False) # el primer valor es ancho el otro es alto 
raiz.geometry("650x500") # diametro
raiz.iconbitmap(".ico")#para colocar una imagen en la barra del titulo tiene que ser .ico
raiz.config(bg="gray")#para darle color de fondo


raiz.mainloop() # mainloop es como un bucle infinito





