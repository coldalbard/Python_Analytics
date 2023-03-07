import random


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

size = int(input("Enter the length of the array: "))
min_el = int(input("Enter the minimum value in the range: "))
max_el = int(input("Enter the maximum value in the range: "))

arr = [random.randint(-10, 10) for i in range(size)]
print(f'Randomly created array:: {arr}')

res_array = [i for i in range(len(arr)) if min_el < arr[i] <= max_el]
print(f'Indexes of elements that correspond to the range: \n{res_array}')