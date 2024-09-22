class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.address = address
        self.age = age

    def walk(self) -> str:
        """
        This method returns a string that indicates the person is walking
        Because walking is healthy, each walking will reduce the age of the person by 1
        """
        self.age -= 1
        return f"{self.name} is walking"

myself = Person("John", 36, "123 Main St")
print(myself.walk())
print(myself.age)

print(myself.walk())
print(myself.age)
