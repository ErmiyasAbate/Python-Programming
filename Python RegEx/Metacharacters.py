import re

txt = "Teh rain in Spain"
print(re.findall("[a-m]", txt))

text = "That will be 59 dollars"
print(re.findall("\d", text))

textOne = "hello planet"
print(re.findall("he..o", textOne))

x = re.findall("^hello", textOne)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

y = re.findall("planet$", textOne)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

print(re.findall("he.*o", textOne))