def CheckMat(text):
    a = []
    f = open('mat.txt')
    for line in f.readlines():
        line = line.split()
        for i in range(len(line)):
            a.append(line[i])
            break

    b = ''
    v = text
    b = b + ' ' + v

    b = b.split()
    flag = False

    for i in range(len(b)):
        if b[i].upper() in a:
            flag = True
            break
    return flag

