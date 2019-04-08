import math

def calculaRaiz(num1):

    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(num1)
opcion1=(int(input("Introduce un número: ")))   

try:
     print(calculaRaiz(opcion1))   

except ValueError as ErrorDeNumeroNegativo:  # como añadir mi propio error   
    print(ErrorDeNumeroNegativo)

print("Programa terminado")
