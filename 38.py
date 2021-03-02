#Re.split()
import re
n = input()
x = re.split("[,.]", n)
for i in range(len(x)):
    print(x[i])