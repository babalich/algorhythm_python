# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
a = [random.randint(0, 20) for i in range(10)]
print(a)

min_i = 0
max_i = 0

for i in range(len(a)):
    if a[i] < a[min_i]:
        min_i = i
    if a[i] > a[max_i]:
        max_i = i

b = a[min_i]
a[min_i] = a[max_i]
a[max_i] = b

print(a)