# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input("Введи число: "))
i = 2
lst = []
while i <= number:
    if number % i ==0:
        lst.append(i)
        number //=i
        i = 2
    else:
        i+=1
print(lst)
