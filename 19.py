#Наименьший положительный
a = [int(i) for i in input().split()]
min = 1001
for x in range(len(a)):
    if a[x]>0:
        if a[x]<min:
            min = a[x]
print(min)