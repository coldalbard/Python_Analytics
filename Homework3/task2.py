import random


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# 1 решение

size_n = int(input("Please enter the length of the array: "))
arr = [random.randint(1, 15) for i in range(size_n)]
print(arr)

x = int(input("Please enter the number N: "))
number = arr[0]
difference = abs(arr[0] - x)

for i in range(1, len(arr)):
    diff = abs(arr[i] - x)
    if diff < difference:
        difference = diff
        number = arr[i]
print(number)


# 2 решение

size_array = int(input("Please enter the length of the array: "))
array = [random.randint(1, 15) for i in range(size_array)]
new_array = []
print(array)
N = int(input("Please enter the number N: "))

for i in range(N):
    i = abs(array[i] - N)
    new_array.append(i)
print(f'{array[new_array.index(min(new_array))]}')