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

# size_n = int(input("Please enter the length of the array: "))
# arr = [random.randint(1, 15) for i in range(size_n)]
# arr[-1] = size_n
# print(arr)
#
# x = int(input("Please enter the number N: "))
# number = 0
#
# for j in range(1, len(arr)):
#     if arr[j - 1] < arr[j] <= x:
#         number = arr[j]
# print(number)