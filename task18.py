# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random as r
number = int(input("Введите искомое число: "))
my_list =  [1,2,3,4,5] #[r.randint(0, 3) for _ in range(r.randint(1, 10))]
min_mod = abs(my_list[0] - number)
div_number = my_list[0]
for  i in my_list:
    if abs(i - number) < min_mod:
        min_mod = abs(i - number)
        div_number = i

print(f' --> {div_number}')