# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# 
# Пример:
# 
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n1 = int(input("Введи число: ",))
n = n1+1
l1 = []
l2 = []
def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print("Последовательность Фибоначчи:")
for i in range(n):
    l1.append(fibonacci(i))
    l2.append(fibonacci(i))

l2[:] = [-i for i in l2]
l2.pop(0)
l1.extend(l2)
l1.sort()

print(l1)