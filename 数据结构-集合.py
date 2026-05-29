# set1={1,2,4,3,1,5,6,6,7,7,7,7}
# print(set1)
# set2={'apple','banana','apple','banana'}
# print(set2)
# set3=set('apple')
# print(set3)
# set4=set([1,2,3,4,5,6,7,6,4,3,2,3,4,1])
# print(set4)
# set5={num for num in range(2,10)}
# print(set5)
#集合中的元素必须是hashable类型
# for elem in set1:
#     print(elem,end='\t')
# print(8 in set1)
# print(1 in set1)


set1={1,2,3,4,5,6,7}
set2={2,4,6,8,10}
set3=set1|set2
print(set1&set2)
print(set1.intersection(set2))
print(set1|set2)
print(set1-set2)
print(set1==set2)
print(set1^set2)
print(set3)
set4={1,2,3,4}
print(set4<set1)
print(set4<=set1)
set1.add(8)
print(set1)
set1.discard(5)
print(set1)
set1.add(5)
set1.remove(5)
print(set1)
# set1.clear()
# print(set1)
a=set1.isdisjoint(set4)
print(a)