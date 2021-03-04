#6.print(int(input()) in range(int(input()),int(input())))
# 6.def n(a,b,c):
#     if a in range(b,c):
#         print(str(a) + " is in the rang")
#     else:
#         print('The number is outside the given range.')
# a,b,c=[int(i) for i in input().split()]
# n(a,b,c)
# 7.def a(s):
#     cnt1,cnt2=0,0
#     for i in s:
#         if i >='a' and i <='z':
#             cnt1 +=1
#         elif i >='A' and i<='Z':
#             cnt2 +=1
#     print("No. of Upper case characters : " + str(cnt2))
#     print("No. of Lower case Characters : " + str(cnt1))
# a(input())
# 8.
#a = [int(i) for i in input().split()]
# print(*set(a))
#8.
#print(set(input().split()))
#8.
# def a(list):
#     b =[]
#     for i in list:
#         if i not in b:
#             b.append(i)
#     print(*b)
# a([int(i) for i in input().split()])
#9.
# def f(n):
#     if n==2:
#         return True
#     elif n>2:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#             else:
#                 return True
#     else:
#         return False
# if f(int(input())):
#     print('Prime')
# else:
#     print("Not a Prime number")
#10
# a = [int(i) for i in input().split()]
# print(list(filter(lambda x:x%2==0,a)))