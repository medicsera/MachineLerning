import numpy as np

"""
Напишите программы, которые создают следующие массивы NumPy:
1. Массив со значениями 1, 7, 13, 105. Посчитайте и выведите на экран размер
памяти, который он занимает. Сохраните массив в текстовый и бинарный файлы.
Затем загрузите его и выведите на экран.
"""

def point_1():
    arr = np.array([1,7,13,105])

    print(f"Массив: {arr}")
    print(f"Размер памяти: {arr.nbytes}")

    np.savetxt("task_1/arr.txt",arr, fmt="%d")

    np.save("task_1/arr.npy", arr)

    load_txt = np.loadtxt('task_1/arr.txt', dtype=np.int32)
    print(f"Загруженный текстовый: {load_txt}")

    load_bin = np.load('task_1/arr.npy')
    print(f"Загруженный бинарный: {load_bin}")


point_1()

"""
2. Три массива: из 10 нулей, 10 единиц, 10 пятерок.
"""
def point_2():
    zeros = np.zeros(10)
    ones = np.ones(10)
    fives = np.full(10,5)
    print(f"Нулевой: {zeros} \nЕдиничный: {ones} \nИз пятерок: {fives}")


point_2()

