a=[]
f = open('mat.txt')
for line in f.readlines():
    line = line.split()
    for i in range(len(line)):
        a.append(line[i])
        break

v = 1
b = ''
while v != '0':
    v = input()
    b = b + ' ' + v

b = b.split()

for i in range(len(b)):
    if b[i].upper() in a:
        print(True)
        break
