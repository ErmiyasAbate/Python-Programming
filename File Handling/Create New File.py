f = open("myfile.txt", "w")
f.write("This is new file!")
f.close()

f = open("myfile.txt", "r")
print(f.read())
f.close()