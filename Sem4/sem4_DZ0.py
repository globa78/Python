# Вычислить число c заданной точностью d
# 
# Пример:
# 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#from math import pi
#d = int(input("Введи точность: "))
#print(round(pi,d))
#
from math import pi

d =  float(input("Введите число для заданной точности числа Пи: "))

d = len(str(d).split('.')[1])
print("число Пи с заданной точностью",(round(pi, d)))