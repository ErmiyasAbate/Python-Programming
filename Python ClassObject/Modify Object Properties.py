class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_function(self):
        print("I am" , self.age, "years old!")

p1 = Person("John", 36)
p1.my_function()

x = int(input("Enter your real age: "))
p1.age = x
p1.my_function()
