import json
my_dict={
    'name':'Jamcc',
    'age':21,
    'life':['AI','Study','work'],
    'cars':[
        {'brand':'BMW','speed':240},
        {'brand':'lamborghin','speed':320},
        {'brand':'hongqi','speed':180}
    ]
}


with open(r"D:\Study_python\data.json",'w+') as file:
    json.dump(my_dict,file)
result=json.dumps(my_dict)
print(result)
print(type(result))
print(my_dict)


with open(r"D:\Study_python\data.json",'r') as file:
    my_data=json.load(file)
    print(my_data)
    print(type(my_data))