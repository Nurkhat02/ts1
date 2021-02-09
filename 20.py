#Сжатие списка
a = [int(i) for i in input().split()]
cnt = 0
for x in range(len(a)):
    if a[x]!=0:
        print(a[x], end=' ')
    else:
        cnt +=1
for y in range(cnt):
    print(0, end=' ')