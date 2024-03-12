                         #### Excepciones Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("No se cumplió")
 ### try except

    try:
        print(numberOne + numberTwo)
        print("No se ha producido un error")
    except TypeError:
    # Se ejecuta si se produce una excepción
        print("Se ha producido un error")

        ### try except else ###

    else:
        # Se ejecuta si no se produce una excepción
        print("La ejecución continúa correctamente")
    finally: # Opcional # Se ejecuta siempre
        print("La ejecución continúa")

    # Excepción por tipo
    try:
        print(numberOne + numberTwo)
        print("No se ha producido un error")
    except TypeError:
        print("Se ha producido un TypeError")
    except ValueError:
        print("Se ha producido un ValueError")













