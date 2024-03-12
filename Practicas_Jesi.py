### Practicas ###
from random import randrange
numero_magico = randrange(100)
respuesta = 0

intentos = 0


#print(respuestas)

while (respuesta != numero_magico):
    respuesta = int(input("Adivina mi numero: "))
    intentos += 1
    if (numero_magico < respuesta):
        print("Mi numero es menor")
        print()
    elif (numero_magico > respuesta):
        print("Mi numero es mayor")
        print()
    elif(numero_magico == respuesta):
        print("Adivinaste el numero, felicidades!")

print(f"Te tardaste {intentos} intentos")







