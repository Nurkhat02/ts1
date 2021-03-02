#Detect Floating Point Number
import re
n = int(input())
for i in range(n):
    n1 =input() 
    x = re.search("^[+-]\d*[.]\d+$",n1)
    print(bool(x))