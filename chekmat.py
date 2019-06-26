def ReadMatData(array):
    f = array
    print(f)
    arr = f.split(' ')
    return CheckMat(arr, array)


def CheckMat(arr, text):
    flag = False
    for i in arr:
        if i in text:
            flag = True
    print(flag)
    return flag

