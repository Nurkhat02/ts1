nums = [int(i) for i in input().split()]
cnt = 0
for x in range(len(nums)-1):
    for y in range(x+1,len(nums)):
        if nums[x]==nums[y]:
            cnt +=1
print(cnt)