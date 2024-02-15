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
    except:
        print("Se ha producido un error")

        ### try except else ###









