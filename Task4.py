# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint

degr = ["\u2070", "\u00B9", "\u00B2", "\u00B3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"]

print("Введите натуральную степень многочлена: ")
k = int(input())

list = [randint(0,100) for i in range(k)]
polynomial = ""

def degress(a: int):
    degree = ""
    temp = str(a)
    for char in temp:
        degree += degr[int(char)] or ""
    return degree

for item in list:
    if (k > 1): polynomial += str(item) + "x" + degress(k) + " + "
    else: polynomial += str(item) + "x" + " + "
    k = k - 1

polynomial += str(randint(0, 100)) + " = 0"

with open('D:\Code\PythonHW_4\Task4.txt', "w", encoding="utf-8") as file:
    file.write(polynomial)

print("Многочлен " + polynomial + " записан в файл.")
