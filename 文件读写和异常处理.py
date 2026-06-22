file = open('致橡树.txt',encoding='utf-8')
print(file.read())

for line in file:
    print(line,end='')





file.close()
