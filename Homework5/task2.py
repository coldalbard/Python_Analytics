# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
a = int(input("Please enter the number A: "))
b = int(input("Please enter the number B: "))
def sum_numbers(a, b):
    if b == 0:
        return a
    return sum_numbers(a + 1, b - 1)
print(f'{a} + {b} = {sum_numbers(a, b)}')


