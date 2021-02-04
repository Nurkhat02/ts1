a = [int(i) for i in input().split()]
max = 0
min = 1000
ind1 = 0
ind2 = 0
for x in range(len(a)):
    if a[x]>max:
        max = a[x]
        ind1 = x 
    if a[x] < min:
        min = a[x]
        ind2 = x
a[ind1],a[ind2]=a[ind2],a[ind1]
for y in range(len(a)):
    print(a[y], end = ' ')