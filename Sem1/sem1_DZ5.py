#  Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. 
# Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21
import math
x_1 = float(input("Введи х1: "))
y_1 = float(input("Введи у1: "))
x_2 = float(input("Введи х2: "))
y_2 = float(input("Введи у2: "))
print('Расстояние между двумя точками: ')
print(math.sqrt((x_1-x_2)**2+(y_1-y_2)**2))