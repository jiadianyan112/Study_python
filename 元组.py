# t1=(12,34,78)
# t2=('A','B',345)
# print(type(t1),type(t2))
# print(len(t1))
# print(t2[1],t2[-1])
# print(t2[:3])
# for elem in t1:
#     print(elem)

# print(35 in t1)

# print(t1+t2)

# t3=('hello',)
# t4=('hello')
# print(type(t3),type(t4))

# a=1,2,3,4,5
# print(a)
# x,y,z,w,*u=a
# print(x,y,z,w,u)

# a,b,*c=range(1,10)
# print(a,b,c)
# a,b,*c=[1,2,3,4]
# print(a,b,c)
# *a,b,c='hello'
# print(a,b,c)
 
# import timeit

# print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
# print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos=('a','b','c','d')
print(list(infos))
frts=['1','2','3','4']
print(tuple(frts))