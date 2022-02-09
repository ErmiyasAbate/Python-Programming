class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def my_function(fname):
        print("Hello my name is " + fname.name)

p1 = Person("John", 36)
p1.my_function()