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

# n = int(input("Please enter the length of the first array: "))
# m = int(input("Please enter the length of the second array: "))
# array1 = {random.randint(-100, 100) for i in range(n)}
# array2 = {random.randint(-100, 100) for i in range(m)}
# result_array = sorted(array1.union(array2))
# print(f'Your first array - {array1}')
# print(f'Your second array - {array2}')
# print(f'Numbers that occur in both sets, going from a smaller to a larger value: \n{result_array}')

# 2 решение

# size1 = int(input())
# size2 = int(input())
# arr1 = [random.randint(-100, 100) for i in range(size1)]
# arr2 = [random.randint(-100, 100) for i in range(size2)]
# res = arr1 + arr2
# print(f'Your first array - {arr1}')
# print(f'Your second array - {arr2}')
# print(f'Numbers that occur in both sets, going from a smaller to a larger value: \n{sorted(set(res))}')

# 3 решение

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
