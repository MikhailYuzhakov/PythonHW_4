# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Введите число:")
numb = int(input())

div_numb = [i+1 for i in range(numb+1) if (numb % (i+1) == 0)] # записываем в массив любые делители числа
div_simple_numb = []

for item in div_numb: # перебираем все делители числа
    divider = item 
    i = 0
    while divider > 0: # ищем кол-во делителей числа (проверка на простоту)
        if (item % divider == 0):
            i = i + 1
        divider = divider - 1
    if (i <= 2):
        div_simple_numb.append(item) # записываем в новый массив простые делители числа

print(div_simple_numb)
        