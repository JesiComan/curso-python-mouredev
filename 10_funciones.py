 #### funciones ####

def my_funciones():
    print("Esto es una función")

my_funciones ()
my_funciones ()
my_funciones ()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)
def sum_two_values(first_values: int, second_values):
    print(first_values / second_values)

def sum_two_values_with_return (first_values, second_values):
    return first_values + second_values

my_result = sum_two_values_with_return(10, 5)
my_result = sum_two_values(1.4, 5.2)
print(my_result)
def print_name (name, surname):
    print(f"{name} {surname}")
    print_name(surname = "Coman", name = "Jesi")


def print_name (name, surname):
    print(f"{name} {surname}")
    print_name(surname="Coman", name="Jesi")
def print_name_with_defaults (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_defaults("Jesica", "Coman")
print_name_with_defaults("Jesica", "Coman", "JesicaComan")

def print_upper_texts(*texts):
    for texts in texts:
        print(texts.upper())
    print_upper_texts("Hola", "Python", "JesicaComan")
    print_upper_texts("Hola")







