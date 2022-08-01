# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

print("Введите кол-во элементов в последовательности: ")
N = int(input())
list = [randint(0,10) for i in range(N)]
uniq_list = []

print("Сгенерированный массив: ")
print(list)

for item_targ in list:
    i = 0
    for item in list:
        if (item_targ == item): i = i + 1
    if (i == 1): uniq_list.append(item_targ)

print("Список неповторяющихся элементов: ")
print(uniq_list)
