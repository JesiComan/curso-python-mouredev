                                   ### classes ###

class MyPerson:
    pass
print(MyPerson)
print(MyPerson())

class Person:
    def __init__(self, name, surname):
      self.name = name
      self.surname = surname

my_person = Person("Jesi", "Coman")




class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    def get_name (self):
        return self._name

    def walk (self):
        print(f"{self.full_name} Está caminando")

my_person = Person("Jesica", "Coman")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Jesica", "Coman", "JesicaComan")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Manuel Gonzalez (El loco de los gatos)"
print(my_other_person.full_name)

my_other_person.full_name = 7150
print(my_other_person.full_name)







