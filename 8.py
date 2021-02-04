a = [int(i) for i in input().split()]
print(a[len(a)-1], end=' ')
for x in range(0,len(a)-1):
    print(a[x], end=' ')