def difference(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Массивы разной длины")

    res = []
    for i in range(len(arr1)):
        dif = abs(arr1[i]-arr2[i])
        res.append(dif)
    return res

a1 = [2,3,6,7,3,8,7,5]
a2 = [4,1,3,6,8,4,2,1]

print("Полученная разность массивов: \n", difference(a1,a2))