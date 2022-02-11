import os

fileName = "demofile3.txt"

if os.path.exists(fileName):
    os.remove(fileName)
else:
    print("The file does not exist")

# os.rmdir("myfolder")