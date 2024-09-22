class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.address = address
        self.age = age

    def walk(self) -> str:
        return f"{self.name} is walking"

myself = Person("John", 36, "123 Main St")
print(myself.walk())

