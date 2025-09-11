import numpy as np

"""
Напишите программу, которая будет решать систему линейных уравнений вида:

a11x+b12y=b1
a21x+b22y=b2

Коэффициенты и правую часть вводит пользователь. Программа выводит решение
системы
"""

def task_3():
    print("Введите коэффиценты через пробел: ")
    cm = np.array([input().strip().split() for _ in range(2)],int)

    print("Введите свободные члены через пробел:")
    fm = np.array(input().strip().split(),int)

    if (np.linalg.det(cm) != 0):
        print(f"Решение: {np.linalg.solve(cm,fm)}")
    else:
        print("Нет решения")

task_3()