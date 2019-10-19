# 4. Определить, какое число в массиве встречается чаще всего.

import random
a = [random.randint(0, 10) for i in range(20)]
print(a)

b = list(set(a))
print(b)


max_rate = [0, 0]   # [0] - частота, [1] - число

for i in range(len(b)):
    rate = 0
    for y in range(len(a)):
        if b[i] == a[y]:
            rate += 1
    if rate > max_rate[0]:
        max_rate[0] = rate
        max_rate[1] = b[i]

print(f'число {max_rate[1]} встретилось {max_rate[0]} раз')
