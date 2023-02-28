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

size = int(input("Please enter the length of the array: "))
num_array = [random.randint(1, 15) for i in range(size)]
print(num_array)

count = 0
k = int(input("Please enter the number N: "))

for j in range(len(num_array)):
    if num_array[j] == k:
        count += 1
print(count)