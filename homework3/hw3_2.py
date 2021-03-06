# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со
# значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5, если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

a = [random.randint(0, 20) for i in range(10)]
print(a)

result = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        result.append(i)

print(f'{result} индексы четных элементов списка (первый элемент списка имеет индекс 0)')