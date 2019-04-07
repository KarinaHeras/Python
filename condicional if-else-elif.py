print("Control de Acceso")
Edad_user=int(input("Introduce tu edad: "))
if Edad_user<18:
    print("No puedes pasar")
elif Edad_user>100:
    print("Edad incorrecta")
else:
    print("Puedes pasar") 

print("El programa ha finalizado")      