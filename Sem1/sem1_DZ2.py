# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = int(input("введи Х: "))
y = int(input("введи Y: "))
z = int(input("введи Z: "))

if not(x or y or z) == (not x and not y and not z):
    print("Утверждение истинно")
else:
    print("Утверждение ложно")