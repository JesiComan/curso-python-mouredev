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














