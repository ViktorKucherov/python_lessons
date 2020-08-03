#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Программа поиска дискриминанта с проверкой на условия вида a * (x**2) + b * x + c'''

from math import sqrt, pow

def root_decision(): # запуск функции поиска корня уравнения
    print('Решим уравнение вида: y = a * (x**2) + b * x + c\n')
    while True:
        a = float(input('Введите а:\n'))
        if a == 0:
            print('Вы ввели недопустимое значение, а - должно быть больше нуля!\n')
        else:
            b = float(input('Введите b:\n'))
            c = float(input('Введите c:\n'))
            if b == 0 and c == 0:
                x = 0
                print(f'Квадратное уравнение имеет единственный корень при {x = }')
                break
            else:
                root_search_with(a, b, c)
                break

def root_search_with(a, b, c): # функция дискриминанта с расчетом значения корней
    d = b ** 2 - 4.0 * a * c
    if d > 0:
        x1 = (-b - sqrt(d)) / (2.0 * a)
        x2 = (-b + sqrt(d)) / (2.0 * a)
        print(f'Корни квадратного уравнения: { x1 = } , { x2 = }')
    elif d == 0:
        x = -b / (2.0 * a)
        print(f'Квадратное уравнение имеет единственный корень при {x = }')
    else:
        print(f'Квадратное уравнение не имеет корней решения')

root_decision()

print('\nEND')