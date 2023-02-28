import random


# Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, 
# причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки

# 1 решение
# плохо понял условие изначально, это решение для 
# нахождения суммы куста(и его соседних) 
# который укажет пользователь 

n = int(input("Please enter the number of bushes: "))
lst = [random.randint(1, 15) for i in range(n)]
print(lst)
res = 0
b = int(input("Please enter the bush from which you want to harvest \n(from neighboring bushes, the harvest will also be harvested):"))

for i in range(n):
    if b == i + 1:
        if b == 1:
            res = lst[i] + lst[i + 1] + lst[-1]
        elif i < n - 1:
            res = lst[i - 1] + lst[i] + lst[i + 1]
        elif b == n:
            res = lst[i - 1] + lst[i] + lst[0]
print(res)


# 2 решение

N = int(input())
array = list()
for i in range(N):
    array.append(random.randint(1, 15))
print(array)
array_count = list()
for i in range(N - 1):
    array_count.append(array[i - 1] + array[i] + array[i + 1])
array_count.append(array[-2] + array[-1] + array[0])
print(max(array_count))