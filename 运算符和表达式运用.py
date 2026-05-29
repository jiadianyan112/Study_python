import math 
# """
# 运算符和表达式运用
# """

# f=float(input('请输入华氏温度：'))
# c=(f-32)/1.8
# print(f'{f:.2f}华氏度={c:.2f}摄氏度')

# """
# 计算圆周长和面积
# """
# radius = float(input('请输入圆的半径：'))
# perimeter =math.pi*2*radius
# area = math.pi*radius**2
# print(f'圆的周长为：{perimeter:.2f},圆的面积为：{area:.2f}')

"""
判断闰年
"""
year =int(input('请输入年份：'))
is_leap_year =(year%4==0 and year%100 !=0) or (year%400==0)
print(f'{is_leap_year =}')