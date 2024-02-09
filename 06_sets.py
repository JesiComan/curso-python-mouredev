# Sets #

my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Jesi", "Coman", 27}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("JesicaComan")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("JesicaComan") # Un set no admite repetidos

print(my_other_set)

print("Coman" in my_other_set)
print("Comancho" in my_other_set)

my_other_set.remove("Coman")
print(my_other_set)

my_other_set.clear() #El clear elimina
print(my_other_set)
print(len(my_other_set))

del my_other_set
#print(my_other_set)

my_set = {"Jesi", "Coman", 27}
my_list = list(my_set)
print(my_list)

my_other_set= {"Tomate", "Hamburguesa", "Queso", "Lechuga", "Cebolla", 3}


my_new_set = my_set.union(my_other_set)
print(my_new_set)

my_new_set = {"Tomate", "Hamburguesa", "Queso", "Lechuga", "Cebolla", 3}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_list = {"Tomate", "Hamburguesa", "Queso", "Lechuga", "Cebolla", 3}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_other_set))
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "Python"}))

print(my_new_set.difference(my_set))
















