# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

result = [0 for i in range(9)]

for i in range(2, 100):
    y = 2
    while y < 10:
        if i % y == 0:
            result[y-1] += 1
        y += 1

for i in range(len(result)):
    if result[i] > 0:
        print(f'{i+1} - {result[i]}')

