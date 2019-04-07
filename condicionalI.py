salario_presidente=int(input("Introduce Salario Presidente"))
print("Salario Presidente: "+ str(salario_presidente))

salario_director=int(input("Introduce Salario Director"))
print("Salario director: "+ str(salario_director))

salario_jefe_area=int(input("Introduce Salario Jefe de area"))
print("Salario jefe de area: "+ str(salario_jefe_area))

salario_administrativo=int(input("Introduce Salario ministrativo"))
print("Salario administrativo: "+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    ("En esta empresa hay una lewinsky jajajaja")    