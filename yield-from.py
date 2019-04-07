def devuelve_ciudades(*ciudades):
   for elemento in ciudades:
    yield  from elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Huelva")
print(next(ciudades_devueltas))