'''
Создайте ряд функций для проведения математических вычислений:
● функция вычисления факториала числа (произведение натуральных чисел от 1
до n). Принимает в качестве аргумента число, возвращает его факториал;
● поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из
трёх чисел, возвращает наибольшее из них;
● расчёт площади прямоугольного треугольника. Принимает в качестве аргумента
размер двух катетов треугольника. Возвращает площадь треугольника.
'''

def factorial():
    a = int(input("Введите число:"))
    f = 1
    for i in range(a + 1):
        if i == 0:
            continue
        else:
            f = f * i
    return(f)

#print(factorial(6))

def maxnum():
    a = list(map(int, input("Введите несколько чисел через пробел:").split()))
    b = max(a)
    return(b)

#print(maxnum())

def righttriangle():
    a = int(input("Введите длинну первого катета:"))
    b = int(input("Введите длинну второго катета:"))
    c = (a * b) / 2
    return(c)

#print(int(righttriangle()))

print(f' Чтобы решить факториал напишите "Факториал" \n Чтобы узнать максимлаьное число из трех, напишите "Максимум" \n Чтобы узнать площадь прямоугольного треугольника, напишите "Треугольник"')
functype = str(input())

if functype == "Факториал":
    print()
    print(factorial())
if functype == "Максимум":
    print(maxnum())
if functype == "Треугольник":
    print(int(righttriangle()))