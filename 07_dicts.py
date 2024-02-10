 #dicts#

my_dict = dict()
print(type(my_dict))

my_other_dict = {"Nombre": "Manuel", "Apellido": "Gonzalez", "Edad": 26, "Altura": "1.74", 1:"Python"}
my_dict = {
    "Nombre": "Manuel",
    "Apellido": "Gonzalez",
    "Edad": 26,
    "Altura": "1.74",
    1:"Python"}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_other_dict.fromkeys(("Nombre", 1)))

my_new_dict = my_other_dict.fromkeys(("Nombre", 1))
print(my_new_dict) # Del Fromkeys Crea un diccionario nuevo, pero que no tiene valores

my_values = my_new_dict.values()

print(type(my_values))
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))
















