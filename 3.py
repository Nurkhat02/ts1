a = [int(i) for i in input().split()]
s = input()
cnt = 1
for x in range(len(a)):
    if a[x]<= int(s):
        cnt +=1
print(cnt)
