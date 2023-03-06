# Задача 26:  Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input("Please enter the number A: "))
b = int(input("Please enter the number B: "))
def Degree(a, b):
    if b > 1:
        b -= 1
        return a * Degree(a, b)
    return a
print(f'{a}^{b} = {Degree(a, b)}')