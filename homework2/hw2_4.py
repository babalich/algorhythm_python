# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,
#  … Количество элементов (n) вводится с клавиатуры

n = int(input('Введите натуральное число'))
sum = 0

for i in range(n):
    k = (-1)**i * (1 / 2**i)
    sum += k
    print(k, ', ', end='')

print(f'\nСумма ряда: {sum}')