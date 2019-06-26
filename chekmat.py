f = open('lyrics.txt', 'r')
lyrics = f.read()
f.close()


def ReadMatData():
    f = open('matdata.txt', 'r')
    arr = []
    for line in f:
        arr.append(line[:-1])
    return CheckMat(arr)


def CheckMat(arr):
    flag = False
    for i in arr:
        if i in lyrics:
            flag = True
    return flag

