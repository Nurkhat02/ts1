#Словарь синонимов
n = int(input())
mydict={}
for i in range(n):
    x,y = input().split()
    mydict[x]=y
    mydict[y]=x
s = input()
print(mydict[s])
