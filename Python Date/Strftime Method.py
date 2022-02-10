import datetime

x = datetime.datetime.now()

x.isocalendar()

print(x.strftime("%B"))
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%j"))
print(x.strftime("%M"))
print(x.strftime("%W"))