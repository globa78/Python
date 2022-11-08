# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# 
# Пример:
# 
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

#     x = float(input("Введите Х:")); 
#     
#     y = float(input("Введите Y:"))
#     
#     result = 0
#     
#     array  = [ 4 , 2 ]
#     
#     array[0,0] = 1
#     array[0,1] = 1
#     
#     array[1,0] = -1
#     array[1,1] = 1
#     
#     array[2,0] = -1
#     array[2,1] = -1
#     
#     array[3,0] = 1
#     array[3,1] = -1
#     
#     for i = 0 and i < array.GetLength(0) and i+=1
#         if (x>0 and array[i,0]>0) and (y>0 and array[i,1]>0):
#             result = i 
#         elif (x<0 and array[i,0]<0) and (y>0 and array[i,1]>0):    
#             result = i 
#         elif (x<0 and array[i,0]<0) and (y<0 and array[i,1]<0):
#             result = i
#         elif (x>0 and array[i,0]>0) and (y<0 and array[i,1]<0):
#             result = i
#     print("Результат" result+1);
""" Напишите программу, которая принимает на вход координаты точки (X и Y), 
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 
Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3  """


def inputKoord(x):
    a = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number
                is_OK = True
                if a[i] == 0:
                    is_OK = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Ты ошибся. Вводить надо числа!")
    return a


def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти плоскости")


koordinate = inputKoord(2)
checkCoordinates(koordinate)