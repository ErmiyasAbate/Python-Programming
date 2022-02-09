class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("My name is " + self.firstname + " " + self.lastname)

class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

p1 = Student("Hermela", "Abate")
p1.printname()