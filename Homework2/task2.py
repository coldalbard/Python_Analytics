# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. 
# Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для
# этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# x = int(input("Please enter the number X: "))
# y = int(input("Please enter the number Y: "))

# # 1 решение
# for i in range(1, 30000):
#     p = x - i
#     if i <= p and i * p == y: 
#         print(i, p)


# # 2 решение
# z = ((x / 2)**2 - y)**0.5
# print(int(x/2 - z), int(x/2 + z))