#Четные индексы
a = [int(i) for i in input().split()]
for x in range(len(a)):
    if x%2==0:
        print(a[x], end=' ')