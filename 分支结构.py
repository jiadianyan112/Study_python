"""
分支结构
"""


# """
# if else 语句
# """
# height =float(input('请输入身高(cm)：'))
# weight=float(input('请输入体重（kg）:'))
# bmi=weight/height**2*10000
# if bmi<18.5:
#     print(f'BMI={bmi:.2f},体重过轻')
# elif 18.5 <= bmi <24:
#     print(f'BMI={bmi:.2f},你的身材很棒！')
# else:
#     print(f'BMI={bmi:.2f},体重过重')


# """
# match case语句 
# """
# small_num = int(input('请输入小写数字：'))
# match small_num:
#     case 0|1|2|3:capital_num ='零' 
#     case 1:capital_num ='一'
#     case 2:capital_num ='二'
#     case 3:capital_num ='三'
#     case 4:capital_num ='四'  
#     case 5:capital_num ='五'
#     case 6:capital_num ='六'
#     case 7:capital_num ='七'
#     case 8:capital_num ='八'
#     case 9:capital_num ='九'
#     case _:print('输入错误！')
# print(f'{small_num}的中文大写是{capital_num}')


# """
# 分段函数求值
# """
# x=float(input('请输入x的值：'))
# if x>5:
#     y=3*x-5
# elif -1<=x<=5:
#     y=x+2
# elif x<-1:
#     y=5*x+3
# else:
#     y=0
# print(f'当x={x}时，y={y}')


# """
# 百分制成绩转化为等级
# """
# score = float(input('请输入成绩：'))
# if score >=90:
#     grade ='A'
# elif 80<=score<90:
#     grade ='B'
# elif 70<=score<80:
#     grade ='C'
# elif 60<=score<70:
#     grade ='D'
# else:
#     grade ='E'
# print(f'{score}分对应的等级为{grade}')



"""
由边长求周长和面积
"""
a =float(input('请输入第一条边长：'))
b =float(input('请输入第二条边长：'))
c =float(input('请输入第三条边长：'))
if a+b>c and a+c>b and b+c>a:
    perimeter =a+b+c
    s=perimeter/2
    area =(s*(s-a)*(s-b)*(s-c))**0.5
    print(f'由{a} {b} {c}三条边构成三角形的周长perimeter={perimeter},面积area={area}')
else:
    print('输入的边长无法构成三角形！')