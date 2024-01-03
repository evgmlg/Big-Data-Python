import random

def max_min(n):

    if n <= 0:
        print("Массив должен быть больше ноля!")

    arr = [random.randint(-100, 100) for i in range(n)]

    print("Исходная матрица: \n", arr)

    max_val = max(arr)
    min_val = min(arr)

    return(max_val, min_val)

outp = max_min(15)

print("Максимальное значение: ", outp[0])
print("Минимальное значение: ", outp[1])