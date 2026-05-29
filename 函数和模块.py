# from math import factorial as f

# def fac(num):
#     result=1
#     for n in range(2,num+1):
#         result *=n
#     return result
# m=int(input('m= '))
# print(f(m))


# def judge_triangle(a,b,*,c):
#     return a+b>c and a+c>b and b+c>a
# print(judge_triangle(1,5,c=8))
# print(judge_triangle(1,8,c=5))


# import random
# def dice(n=2):
#     total=0
#     for _ in range(1,n+1):
#         total=total+random.randrange(7)
#     return total
# print(dice())
# print(dice(5))

# def add(a=1,b=2,c=3):
#     return a+b+c
# print(add())
# print(add(1,5))
# print(add(2,5,7))


# def add(*num):
#     sum=0
#     for val in num:
#         if type(val) in (int,float):
#             sum+=val
#     return sum
# print(add())
# print(add(1,2,3,4,5,6,'a',12.345))

# def rkey(**keywords):
#     print(keywords)
# rkey(num= 1,rank='sun')

import hello as q1
import hi as q2
q1.put()
q2.put()