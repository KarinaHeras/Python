def divide():
    try:
        opcion1=(float(input("introduce el primer número: ")))   #sustituyo el in por float
        opcion2=(float(input("introduce el segundo número: ")))

        print("La divicion es: " + str(opcion1/opcion2))
    except ValueError:
        print("El valor introducido es erróneo") 
    except ZeroDivisionError:
        print("No se puede dividir entre 0!") 
    finally:
        print("Cálculo finalizado")  
divide()                