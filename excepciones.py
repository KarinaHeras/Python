def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplica(num1,num2):
    return num1*num2

def divide(num1,num2):
    try:                  #captura de excepcion    
        return num1/num2  
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion errónea"
while True:
    try:
        opcion1=(int(input("Indroduce el primer número:  ")))
        opcion2=(int(input("Indroduce el segundo número:  ")))
        break
   
    except ValueError:
    print("Los valores introducidos no son correcto. Intentarlo nuevamente") 
      
operacion=input("Indroduce la opción a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
    print(suma(opcion1,opcion2))

elif operacion=="resta":
    print(resta(opcion1,opcion2))

elif operacion=="multiplica":
    print(multiplica(opcion1,opcion2))    

elif operacion=="divide":
    print(divide(opcion1,opcion2))   

else:
    print("Operación no completada")

print("Operación ejecutada. Continuación de ejecución del programa")       

