### Loops ####

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi conditión es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
  my_condition += 2
if my_condition == 15:
  print("Se detiene la ejecución")

print(my_condition)
print("Se detiene la ejecución")

print("La ejecución continúa")

                   ### For ###

   # Sirve para alterar un listado de elementos

my_list = (35, 24, 62, 52, 30, 30, 17)

for element in my_list:
    print(element)
my_tuple = (27, 1.65, "Jesi", "Jesi", "Coman", 70, 80, 80, 80)

for element in my_tuple:
    print(element)

my_set = {"Jesi", "Coman", 27}

for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Manuel",
    "Apellido": "Gonzalez",
    "Edad": 26,
    "Altura": "1.74",
    1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
        print("Se ejecuta")
        break
    elif element == 1:
        print("element vale 1")
    else:

        print("El bucle for para mi diccionario ha finalizado")

        print("La ejecución continúa")




















