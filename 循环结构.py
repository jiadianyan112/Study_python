import time 
import random
# print('Hello,World!')
# time.sleep(1)
# print('Hello,Python!')
# time.sleep(1)
# print('Hello,Java!')
# time.sleep(1)
# print('Hello,C++!')
# time.sleep(1)
# print('Hello,Go!')
# time.sleep(1)

#total=0

# '''
# for循环
# '''
# for i in range(2,101,2):
#     total=total+i
# print(f'total={total}')

# """
# while循环,break,continue
# """
# i=0
# while 1:
#     total=total+i
#     i+=1
#     if i>100:
#         break
#     if i%2 !=0:
#         continue

# print(total)

"""
嵌套的循环结构
"""

# #打印乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end ='\t')
#     print()


# #判断素数
# num = int(input('请输入一个整数：'))
# is_prime=True
# end = int(num**0.5)+1
# for i in range(2,end):
#     if num%i==0:
#         is_prime =False
#         break
# if is_prime:
#     print(f'{num}是一个素数')
# else:
#     print(f'{num}不是一个素数')


# #最大公约数1
# a = int(input('请输入第一个数：'))
# b = int(input('请输入第二个数：'))
# i=min(a,b)
# while i>=1:
#     if a%i==0 and b%i==0:
#         print(f'{a}和{b}的最大公约数为{i}')
#         break
#     else:
#         i=i-1

# #最大公约数2
# x=int(input('请输入第一个数：'))
# y=int(input('请输入第二个数：'))
# a=x
# b=y
# while a%b !=0:
#     a,b=b,a%b
# print(f'{x}和{y}的最大公约数为{b}')

# #猜数字游戏

# num = random.randint(1,100)
# guess_num =int(input('请输入猜测的数字'))
# i=1
# while guess_num != num:
#     i+=1
#     if guess_num>num:
#         print('大了，继续猜')
#     if guess_num<num:
#         print('小了，继续猜')
#     guess_num =int(input('请输入猜测的数字'))
# print(f'恭喜你Jam！你猜对了！，你猜了{i}次')



# #输出100以内的素数
# num=2

# while num<101:
#     is_prime=True
#     end = int(num**0.5)+1
#     for i in range(2,end):
#         if num%i==0:
#             is_prime =False
#             break
#     if is_prime:
#         print(num,end='\t')
#     num+=1


# #斐波那契数列
# a=1
# b=1
# i=1
# print(a,end='\t')
# print(b,end='\t')
# while i<20:
#     a,b=b,a+b
#     i=i+1
#     print(b,end='\t')


# #寻找水仙花数
# def count_digits(n):
#     return len(str(n))
# for x in range(100,10000):
#     i=count_digits(x)
#     sum=0
#     a=x
#     while i>0:
#         sum=sum+(a%10)**count_digits(x)
#         a=a//10
#         i=i-1
        
#     if x == sum:
#         print(x)


# #百钱百鸡问题

# for a in range(0,21):
#     for b in range(1,34):
#         c=3*(100-5*a-3*b)
#         if c<0:
#             break
#         print(f'公鸡有{a}只，母鸡有{b}只，小鸡有{c}只')




#CRAPS赌博游戏
money=1000
while money>0:
    print(f'你的资产为{money}元')
    stake=int(input('Jam请下注：'))
    a=random.randint(1,6)
    b=random.randint(1,6)
    print(f'你摇出了{a}点和{b}点')
    count = a+b
    if count==7 or count ==11:
        money=money+stake
        print('你赢了！')
    elif count==2 or count ==3 or count==12:
        money=money-stake
        print('你输了···')
    else:
        print('没人获胜···游戏继续')
        while 1:
            c=random.randint(1,6)
            d=random.randint(1,6)
            print(f'你摇出了{c}点和{d}点')
            count1=c+d
            if count1==7:
                money=money-stake
                print(f'你输了···')
                break
            elif c==a or c==b or d==a or d==b:
                money=money+stake
                print(f'你赢了！')
                break
            else:
                print('没人获胜···游戏继续')
                continue
    
print('Jam你破产了···')


