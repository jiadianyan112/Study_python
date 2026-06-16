import csv
import random

with open(r'D:\Study_python\score.csv','w',newline='') as file:
    writer=csv.writer(file,delimiter='|',quoting=csv.QUOTE_ALL)
    writer.writerow(['name','Chinese','Math','English'])
    names=['Linda','Jack','Messi','Trump']
    for name in names:
        scores = [random.randrange(60,101) for _ in range(3)]
        scores.insert(0,name)
        writer.writerow(scores)
    

with open(r'D:\Study_python\score.csv','r') as file:
    reader=csv.reader(file,delimiter='|')
    for data_list in  reader:
        print(reader.line_num,end='\t')
        for elem in data_list:
            print(elem,end='\t')
        print()

