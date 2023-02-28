import random


# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в 
# порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# 1 решение

n = int(input())
m = int(input())
array1 = {random.randint(-100, 100) for i in range(n)}
array2 = {random.randint(-100, 100) for i in range(m)}
result_array = sorted(array1.union(array2))
print(array1)
print(array2)
print(result_array)
