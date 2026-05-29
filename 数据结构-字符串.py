"""
字符串的定义
"""

# s1='Hello,world!'
# s2="你好，🐷"
# s3='''hi
# come on
# you'''#多行字符串
# print(s1)
# print(s2)
# print(s3)


# s1='\'hello,你好\''
# print(s1)
# s2='\\hello,你好\\'
# print(s2)

# s1='it is \time \to \t\\read \now'#\t是制表符（table），\n是换行符（new line），\r是回车符（carriage return）相当于让输出回到了行首。
# s2=r'\it \is \time \to \read \now'
# print(s1)
# print(s2)

# print(chr(121))
# print(chr(24310))


'''
字符串的运算
'''
# s1= 'hello'+'hi'+'come'*3
# print(s1)
# s1=s1+'测试'
# print(s1)
# print(ord('延'),ord('佳'),ord('政'))
# print(chr(24310),chr(20339),chr(25919))

# s1='abcde,fghi,jklmn'
# s2='abcdef'
# print(s1<s2)
# print('a'not in s1)
# print(len(s1))
# print(s1[::-1])
# for elem in s1 :
#     print(elem,end='\t')


# print(s1.capitalize())
# print(s1.title())
# print(s1.upper())
# s2='ABCDEFG'
# print(s2.lower())
# print(s2)

# s1='abcdefghigk'
# print(s1.rfind('kg'))
# print(s1.index('fg'))


# s1 = 'abcdefghijk'
# print(s1.startswith('ab'))
# print(s1.endswith('jk'))
# print(s1.isdigit())
#isdigit用来判断字符串是不是完全由数字构成的
#isalpha用来判断字符串是不是完全由字母构成的
#isalnum用来判断字符串是不是由字母和数字构成的



'''
格式化
'''
# s1='abcde'
# print(s1.center(19,'*'))
# print(s1.center(20,'*'))
# print(s1.rjust(20,'*'))
# print(s1.ljust(20,'0'))
# print(s1.zfill(20))

#修建
# s1='``abcde`````'
# print(s1.strip('`'))

#替换
# s1='abcdefgdedefd'
# print(s1.replace('d','*'))
# print(s1.replace('d','*',5))

#拆分与合并
# s1='abcwdewfghwi'
# print(s1.split('w'))
# print('*'.join(s1.split('w')))

#编码与解码
name='延佳政'
b=name.encode('utf-8')
print(b)
print(b.decode('utf-8'))