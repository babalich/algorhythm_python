from sys import getsizeof
import random
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти

def get_size(value):
    result = 0
    for i in value:
        result += getsizeof(i)
    print(f'(Объем памяти: {result})')

def most_common_0(value):
    b = list(set(value))
    print(b)
    max_rate = [0, 0]  # [0] - частота, [1] - число

    for i in range(len(b)):
        rate = 0
        for y in range(len(a)):
            if b[i] == a[y]:
                rate += 1
        if rate > max_rate[0]:
            max_rate[0] = rate
            max_rate[1] = b[i]
    variables_list = [b, max_rate, rate, i, y, value]
    get_size(variables_list)
    print(f'число {max_rate[1]} встретилось {max_rate[0]} раз')

def most_common_1(value):
    N = len(value)
    num = value[0]
    max_frq = 1
    for i in range(N - 1):
        frq = 1
        for k in range(i + 1, N):
            if value[i] == value[k]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = value[i]
    variables_list = [N, num, max_frq, i, k, frq, value]
    get_size(variables_list)
    if max_frq > 1:
        print(max_frq, 'раз(а) встречается число', num)
    else:
        print('Все элементы уникальны')

def most_common_2(value):
    result = sorted([(i, value.count(i)) for i in set(value)], key=lambda t: t[1])[-1]
    variables_list = [result, value]
    get_size(variables_list)
    print(f'(Число {result[0]} встречается {result[1]} раз)')

# В выводе видно, что последний алгоритм использует наименьшее количество памяти.
# Win 10 x64
a = [random.randint(0, 10) for i in range(20)]
print(a)

most_common_0(a)
print('\n')
most_common_1(a)
print('\n')
most_common_2(a)




