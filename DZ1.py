# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# num =  int (input ("Введите число: ")) 

# if num >= 1 and num <=5:
#     print ('нет')

# elif num >= 6 and num <= 7: 
#     print ('да')

# else: 
#     print ('введено неккоректное число')

# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Предикату можно заменить на понятие "бит". 
# Должна получиться таблица истинности.

# print('X Y Z')
# for X in range(0, 2):
#     for Y in range(0, 2):
#         for Z in range(0, 2):
#             if not(X or Y or Z) == (not (X) and not Y and not Z):
#                 print (X, Y, Z)

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите число: '))
# y = int(input('Введите число: '))
# if x > 0 and y > 0:
#         print('1')
#         if x > 0 and y < 0:
#             print('4')
#             if x < 0 and y < 0:
#                 print('3')
#                 if x < 0 and y > 0:
#                     print('2')

# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# num_quart = int(input('Введите номер четверти "число от 1 до 4": '))
# if num_quart < 2 and  num_quart > 0:
#     print('x > 0 and y > 0')
# elif num_quart < 3 and  num_quart > 1:
#         print('x < 0 and y > 0')
# elif num_quart < 4 and  num_quart > 2:
#             print('x < 0 and y < 0')
# elif num_quart < 5 and  num_quart > 3:
#                 print('x > 0 and y < 0')
# else:
#     print('Введите корректное число')   

# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09

# - A (7,-5); B (1,-1) -> 7,21

# import math
# x1 = int(input('введите координату x1: '))
# x2 = int(input('введите координату x2: '))
# y1 = int(input('введите координату y1: '))
# y2 = int(input('введите координату y2: '))
# print (f'расстояние {math.sqrt((y1-x1)**2+(y2-x2)**2)}')