#1.
# def f(n,m):
#     return max(n,m)
# a = [int(i) for i in input().split()]
# print(f(a[0],f(a[1],a[2])))
########################################################
#2.
# def aa(list):
#     return sum(list)
# a = [int(i) for i in input().split()]
# print(aa(a))
########################################################
# 3.
#def n(list):
#     ans = 1
#     for i in list:
#         ans *=i
#     return ans
# a = [int(i) for i in input().split()]
# print(n(a))
########################################################
#4.
# def f(a):
#     ans = ''
#     for i in range(len(a)-1,-1,-1):
#         ans+=a[i]
#     return ans
# a= input()
# print(f(a))
#4
#print (input()[::-1])
#4.
# def f(a):
#     print(a[::-1])
# f(input())
#5.
# def f(n):
#     a = 1
#     for i in range(1,n+1):
#         a *=i
#     print(a)
# f(int(input()))
#5.
# def fn(a):
#     if a==0:
#         return 1
#     else:
#         return a*fn(a-1)
# print(fn(int(input())))
#5
# import math
# print(math.factorial(int(input())))