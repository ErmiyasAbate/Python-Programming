import re

txt = "The rain in spain"
x = re.search("^The.*spain$", txt)

print(x)
if x:
    print("YES! We have a match!")
else:
    print("No match")