# новый вариант
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


n = (int(input("Введи число: ",))+1)
l1 = []
[l1.append(fibonacci(i)) for i in range(n)]
l2 = []
[l2.append(fibonacci(i)) for i in range(n)]

l2 = list(map(lambda i: -i, l2))
l2.pop(0)
l1.extend(l2)
l1.sort()

print("Последовательность Фибоначчи:\n", l1)

# Задайте список из n чисел последовательности (1+ 1/n)n и выведите на экран их сумму.
# Например, для n = 4 последовательность будет иметь вид [2.0, 2.25, 2.37037037037037, 2.44140625]
# сумма будет равна 9.06177...

n = int(input("Введи число N: "))
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def Maximal(l1):
    max_ = l1[0]
    for ele in l1:
        if ele > max_:
            max_ = ele
    return max_


def Minimal(l1):
    min_ = l1[0]
    for ele in l1:
        if ele < min_ and min_ != 0:
            min_ = ele
        else:
            min_ = l1[1]
    return min_

i = [float(x) for x in input().split()]
l1 = []
[l1.append(round(bb%1,3)) for bb in i]
l1.sort()

print(Maximal(l1)-Minimal(l1))
