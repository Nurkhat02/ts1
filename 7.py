a = [int(i) for i in input().split()]
b = len(a) - 1 
if len(a)%2==0:
    n = len(a)-1
else:
    n=len(a)-2
for x in range(0,n,2):
    print(a[x+1], a[x], end = ' ')
if len(a)%2!=0:
    print(a[b])