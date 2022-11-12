# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Введите номер четверти: "))
array1  = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1],[3,0],[3,1]]
array1[0] = 1
array1[1] = 1
array1[2] = -1
array1[3] = 1
array1[4] = -1
array1[5] = -1
array1[6] = 1
array1[7] = -1
x = 0
y = 0
if number == 1:
    minx = array1[0]
    miny = array1[1]
if number == 2:
    minx = array1[2]
    miny = array1[3]
if number == 3:
    minx = array1[4]
    miny = array1[5]
if number == 4:
    minx = array1[6]
    miny = array1[7]
maxx = ""
maxy = ""
if minx>0:
    maxx = "бесконечность"
else:
    maxx = "-бесконечность"
if miny>0:
    maxy = "бесконечность"
else:
    maxy = "-бесконечность"
print(f'"от x = {minx} до x = {maxx}"')
print(f'"от y = {miny} до y = {maxy}"')
