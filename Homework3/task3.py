# Задача 20: В настольной игре Скрабл (Scrabble) каждая
# буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость
# введенного пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только
# английские, либо только русские буквы.
# dct = {abs(x - item): item for item in lst} - код для создания словаря

# 1 решение
# text = input().upper("Please enter the word: ")
# counter = 0
# for i in text:
#     if i == "A" or i == "E" or i == "I" or i == "O" \
#             or i == "U" or i == "L" or i == "N" or i == "S"\
#             or i == "T" or i == "R":
#         counter += 1
#     if i == "D" or i == "G":
#         counter += 2
#     if i == "B" or i == "C" or i == "M" or i == "P":
#         counter += 3
#     if i == "F" or i == "H" or i == "V" or i == "W" or i == "Y":
#         counter += 4
#     if i == "K":
#         counter += 5
#     if i == "J" or i == "X":
#         counter += 8
#     if i == "Q" or i == "Z":
#         counter += 10
#
#     if i == "А" or i == "В" or i == "Е" or i == "И" \
#             or i == "Н" or i == "О" or i == "Р" or i == "С" or i == "Т":
#         counter += 1
#     if i == "Д" or i == "К" or i == "Л" or i == "М" or i == "П" or i == "У":
#         counter += 2
#     if i == "Б" or i == "Г" or i == "Ё" or i == "Ь" or i == "Я":
#         counter += 3
#     if i == "Й" or i == "Ы":
#         counter += 4
#     if i == "Ж" or i == "З" or i == "Х" or i == "Ц" or i == "Ч":
#         counter += 5
#     if i == "Ш" or i == "Э" or i == "Ю":
#         counter += 8
#     if i == "Ф" or i == "Щ" or i == "Ъ":
#         counter += 10
# print(counter)

# 2 решение
# dictionary = {1:'AEIOULNSTRАВЕИНОРСТ',
#       	2:'DGДКЛМПУ',
#       	3:'BCMPБГЁЬЯ',
#       	4:'FHVWYЙЫ',
#       	5:'KЖЗХЦЧ',
#       	8:'JZШЭЮ',
#       	10:'QZФЩЪ'}
# new_text = input("Please enter the word: ").upper()
# print(sum([k for i in new_text for k, v in dictionary.items() if i in v]))