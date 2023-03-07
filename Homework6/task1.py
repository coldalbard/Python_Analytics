# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input("Enter the first element of the array: "))
d = int(input("Enter the difference of the array elements: "))
n = int(input("Enter the number of items: "))
arr = []
for i in range(n):
    arr.append(a + i * d)
print(f'Your array: {arr}')
