# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# 
# Пример:
# 
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
i = [float(x) for x in input().split()]
l1 = []
for j in i:
    bb = j % 1
    l1.append(round(bb, 3))

l1.sort()

def Maximal(l1): 
    max_ = l1[0]
    for ele in l1:
        if ele > max_:
           max_ = ele
    return max_ 

def Minimal(l1): 
    min_ = l1[0]
    for ele in l1:
        if ele < min_ and min_!=0:
           min_ = ele
        else:
            min_= l1[1]
    return min_

a = Maximal(l1)
b = Minimal(l1)

print(a-b)