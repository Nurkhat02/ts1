a = [int(i) for i in input().split()]
cnt = 1
for x in range(0,len(a)-1):
    if a[x]!=a[x+1]:
        cnt +=1
print(cnt)