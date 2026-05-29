# number={1:'数字1',
#         2:'数字2',
#         3:'数字三'}
# print(number)

# person=dict(name='Jamcc',age=21,height=175,weight=65)
# print(person)

# item1=dict(zip('ABCDE','12345'))
# print(item1)

# item2={a:a*2 for a in range(1,10)}
# print(item2)
# print(len(item2))

# for num in item2:
#     print(num)


#字典的运算

# person1 = {
#     'name': '王大锤',
#     'age': 28,
#     'height': 168,
#     'weight': 60,
#     'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
#     'car': {
#         'brand': 'BMW X7',
#         'maxSpeed': '250',
#         'length': 5170,
#         'width': 2000,
#         'height': 1835,
#         'displacement': 3.0
#     }
# }

#print(person)
# print('name' in person)
# print('tel' in person)
# print(person['name'])
# person['name']='张三'
# print(person['name'])

# for key in person:
#     print(f'{key}:\t{person[key]}')

# print(person.get('name'))
# print(person.get('sex'))
# print(person.get('sex',True))
# print(person.keys())
# print(person.values())
# print(person.items())
# # for key,value in person.items():
#     print(f'{key}:\t{value}')

# person2={'age':18,'sex':'man'}
# person1.update(person2)
# print(person1)

# print(person1.pop('age'))
# print(person1.popitem())
# person1.clear()
# print(person1)

# del person1['car']
# print(person1)


#字典的应用

# sentence=input('请输入一句英文语句：')
# counter = {}
# for key in sentence:
#     if 'A'<= key<='Z' or 'a' <= key <= 'z':
#         counter[key]=counter.get(key,0)+1
# sorted_key=sorted(counter,key=counter.get,reverse=True)
# for key in sorted_key:
#     print(f'{key}出现了{counter[key]}次')


stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

num={key:value for key,value in stocks.items() if value>=100}
print(num)