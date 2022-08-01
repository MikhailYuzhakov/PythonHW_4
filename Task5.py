# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

pol_1 = ""
pol_2 = ""
listPol_1 = []
listPol_2 = []
sumPol = []
degr = ["\u2070", "\u00B9", "\u00B2", "\u00B3", "\u2074", "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"] # таблица кодов для знаков степеней

with open('D:\Code\PythonHW_4\Task5_1.txt', mode = "r", encoding = "utf-8") as file:
    pol_1 = file.read()

with open('D:\Code\PythonHW_4\Task5_2.txt', mode = "r", encoding = "utf-8") as file:
    pol_2 = file.read()

print("Многочлен 1:", pol_1)
print("Многочлен 2:", pol_2)

# функция для приведения строки к необходимому виду и записи элементов строки в список
def StrToList(usrStr):
    list = []
    usrStr = usrStr.replace(" ", "") # удаляем все пробелы
    usrStr = usrStr.split("=") # откидываем часть многочлена после знака равно
    usrStr = usrStr[0].split("+") # разбиваем многочлен

    # в каждом элементе отделяем коэффициент от неизвестного Х
    i = 0
    for item in usrStr:
        a = item.split("x")
        list.append(a[0])
        if (len(a) > 1): list.append(a[1])
    
    # заменяем значение степеней в utf-8 на обычные цифры
    for i in range(len(list)-1):
        for j in range(len(degr)-1):
            if list[i] == degr[j]: list[i] = str(j)
            if list[i] == '': list[i] = '1'

    if (len(list) % 2 != 0): list.append('0')
    return list

# функция расставляет коэффициенты многолчена на позицию элемента списка, соответствующую его степени
def FormatList(usrList):
    pos = []
    coeff = []
    # заполняем список позиций и список коэффициентов (на нечетных позициях в исходном массиве стоят позиции, на четных коэффициенты)
    for i in range(len(usrList)):
        if i % 2 == 0: coeff.append(usrList[i])
        else: pos.append(usrList[i])

    res = [0 for i in range(len(pos)+1)] # заполняем список для результата
    pos = list(map(int, pos)) # массив позиций преобразуем в массив int

    # расставляем коэффициенты в массиве
    j = 0
    for i in pos:
        res[i] = coeff[j]
        j = j + 1
    
    return res

# функция для замены целого числа за знак степени
def degress(a: int):
    degree = ""
    temp = str(a)
    for char in temp:
        degree += degr[int(char)] or ""
    return degree

# функция для преобразования массива в строку с полиномом
def ListToPol(usrList):
    poly = ""
    for i in range(len(usrList)-1, -1, -1):
        if (i == 0): poly += str(usrList[i])
        if (i == 1): poly += str(usrList[i]) + "x" " + "
        if (i > 1): poly += str(usrList[i]) + "x" + degress(i) + " + "
    poly += " = 0"
    return poly

listPol_1 = list(map(int, FormatList(StrToList(pol_1))))
listPol_2 = list(map(int, FormatList(StrToList(pol_2))))

if (len(listPol_1) < len(listPol_2)): minLen = len(listPol_1)
else: minLen = len(listPol_2)

for i in range(minLen):
    sumPol.append(listPol_1[i] + listPol_2[i])

print("Сумма многочленов: ", ListToPol(sumPol))