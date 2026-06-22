"""
动态属性
"""
# class student:
#     __slots__ = ('name','age')
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def study(self,course_name):
#         print(f'{self.name}正在学习{course_name}.')

# stu = student('Jam',20)
# stu.study('python程序设计')
# stu.sex='男'

"""
静态方法和类方法
"""

# class triangle:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     @staticmethod
#     def is_valid(a,b,c):
#         "判断三条边能否构成三角形(静态方法)"
#         return a+b>c and a+c>b and b+c>a
    
#     # @classmethod
#     # def is_valid(cls,a,b,c):
#     #     "判断三条边能否构成三角形(静态方法)"
#     #     return a+b>c and a+c>b and b+c>a
    
#     def perimeter(self):
#         return self.a+self.b+self.c
    
#     def area(self):
#         p=self.perimeter()/2
#         return (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
    

# if triangle.is_valid(3,4,5):
#     t=triangle(3,4,5)
#     print(f'周长：{t.perimeter()}')
#     print(f'面积：{t.area()}')
# else:
#     print('不能构成三角形')
 

"""
继承和多态
"""

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print(f'{self.name}正在吃饭')

    def sleep(self):
        print(f'{self.name}正在睡觉')

class student(person):
    def __init__(self,name,age):
        super().__init__(name,age)
    def study(self,course_name):
        print(f'{self.name}正在学{course_name}')
    
class teacher(person):
    def __init__(self,name,age,title):
        super().__init__(name,age)
        self.title=title
    def teach(self,course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}')

stu1= student('白远方',21)
stu2 = student('狄仁杰',22)
tea1=teacher('武则天',30,'教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')