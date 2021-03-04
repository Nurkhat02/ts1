# 11.def p(a):
#     b = []
#     sum = 0
#     for i in range(1,a+1):
#         if a%i==0:
#             b.append(i)
#     for i in b:
#         sum +=i
#     if sum/2==a:
#         return True
#     else:
#         return False
        
# if p(int(input())):
#     print('Yes')
# else:
#     print("NO")
#11.
# a = int(input())
# print(sum(i for i in range(1,a) if a%i==0)==a)
#12
# def a(s):
#     if s[::-1]==s:
#         return True
#     else:
#         return False
# if a(input()):
#     print('yes')
# else:
#     print('no')
#14.
# def f(x):
#     b = set()
#     for i in range(len(x)):
#         if x[i]>='a' and x[i]<='z':
#             b.add(x[i])
#     if len(b)==26:
#         print('YES')
#     else:
#         print('NO')
# a = input()
# x = a.lower()
# f(x)
#14.
# print(set('abcdefghijklmnopqrstuvwxyz')<=set(input().lower()))
#14.
# import string, sys
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())
# print ( ispangram('The quick brown fox jumps over the lazy dog')) 
#15.
# a = [str(i) for i in input().split('-')]
# a.sort()
# print(*a,sep = '-')
#16
# def f():
#     for i in range(1,31):
#         yield i**2
# print(*list(f()))
#18
# exec('print(2**3)')
