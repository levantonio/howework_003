# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
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
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

one_point = "AEIOULNSTRАВЕИНОРСТ"
two_points = "DGДКЛМПУ"
three_points = "BCMPБГЁЬЯ"
four_points = "FHVWYЙЫ"
five_points = "KЖЗХЦЧ"
eight_points = "JXШЭЮ"
ten_points = "QZФЩЪ"

word = input("Введите слово: ")
count = 0
for letter in word:
    if letter in one_point.lower():
        count += 1
    elif letter in two_points.lower():
        count += 2
    elif letter in three_points.lower():
        count += 3
    elif letter in four_points.lower():
        count += 4
    elif letter in five_points.lower():
        count += 5
    elif letter in eight_points.lower():
        count += 8
    elif letter in ten_points.lower():
        count += 10

print(f'УРА! Слово {word}, вырывается вперёд со счетом {count} очков.')