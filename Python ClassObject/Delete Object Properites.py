class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.name
p1.my_function()