#Re.findall() & Re.finditer()
import re
n = input()
x= re.findall("^[aeiou]([AEIOUaeiuo]{2,})(?=[^aeoiu])",n)
for i in range(len(x)):
    print(x[i])