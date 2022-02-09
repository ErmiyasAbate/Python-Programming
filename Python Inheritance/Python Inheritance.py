class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("My name is " + self.firstname + " " + self.lastname)

p1 = Person("Ermiyas", "Abate")
p1.printname()

class Student(Person):
    pass

p2 = Student("Hermela", "Abate")
p2.printname()