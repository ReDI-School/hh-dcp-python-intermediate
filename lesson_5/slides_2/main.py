class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.address = address
        self.age = age

myself = Person("John", 36, "123 Main St")
print(myself.name)

my_neighbor = Person("Jane", 25, "456 Elm St")
print(my_neighbor.name)

