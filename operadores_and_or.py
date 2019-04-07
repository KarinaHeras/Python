print("Programa de becas Año 2019")
distancia_escuela=int(input("Introduce la distanacia de la escuela en km ")) 
print(distancia_escuela)

numeros_hermanos=int(input("Introduce el Nº de hermanos en el centro "))
print(numeros_hermanos)

salario_familiar=int(input("Introdce el salario anual bruto  "))
print(salario_familiar)

if distancia_escuela>40 and numeros_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")    