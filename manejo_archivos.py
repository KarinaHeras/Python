from io import open

archivo_texto=open("archivo.txt","r")

archivo_texto.seek(len(archivo_texto.read()))
print(archivo_texto.read())




