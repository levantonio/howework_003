# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
import random as r
number = int(input("Введите искомое число: "))
my_list = [r.randint(0, 3) for _ in range(r.randint(1, 10))]
print(my_list)
if number in my_list:
    print(f'Число {number} встречается в списке -> {my_list.count(number)} раз.' )
else:
    print(f'числа {number} нет в списке((( ')