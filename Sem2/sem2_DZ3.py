# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
N = int(input("Введите размер списка: "))
spam = list(range(-N, N+1))
print(spam)
index = int(input("Введите элемент для произведения:"))
index1 = int(input("Введите элемент для произведения:"))
index2 = int(input("Введите элемент для произведения:"))
prod = spam[index]*spam[index1]*spam[index2]
print(f'Произведение элементов {spam[index]} * {spam[index1]} * {spam[index2]} = ', prod)