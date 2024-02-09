# listas #

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 15, 30, 86]

print(my_list)
print(len(my_list))

my_other_list = [27, 1.65, "Jesi", "Coman"]
print(my_other_list)
print(type(my_other_list))

print(type(my_other_list[0]))
print(type(my_other_list[1]))
print(type(my_other_list[-3]))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.pop()
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

my_other_list.insert(2, "Rojo")
print(my_other_list)

my_new_list = my_list.copy()
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])





















