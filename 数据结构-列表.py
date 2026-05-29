import math
# #列表概念引出
import random
# a=b=c=d=e=f=0
# for i in range(1,6001):
#     data=random.randint(1,6)
#     match data:
#         case 1:a=a+1
#         case 2:b=b+1
#         case 3:c=c+1
#         case 4:d=d+1
#         case 5:e=e+1
#         case 6:f=f+1
# a=a/6000
# b=b/6000
# c=c/6000
# d=d/6000
# e=e/6000
# f=f/6000
# print(f'1:{a}次，2:{b}次，3:{c}次，4:{d}次，5:{e}次，6:{f}次')


# item1=[1,2,3,4,5,6,7,8]
# print(type(item1))
# item2=['python','C','Java']
# print(item2)
# item3=list(range(1,10))
# print(item3)
# item4=list('Yan Jia')
# print(item4)
# print(item1+item2)
# print(item1*2)
# print(10 in item1)

# item5=['a,b,c,d']
# print(item5)
# print(1 not in item1)

# item=[1,2,3,4,5,6,67,8,8,89]
# print(item[-1])
# print(item)
# print(item[2:8:2])
# print(item[-1:-8:-2])
# print(item[::])
# item[1:2]=['hi','hi']
# print(item)

# item1=[1,2,3,4,5]
# item2=[1,2,3,4]
# print(item1<item2)
# for i in range(len(item1)):
#     print(item1[i],end='\t')

count=[0]*6
for i in range(1,6001):
    data=random.randint(1,6)
    count[data-1]+=1
print(count)