# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
n = 25

num1 = n*(n+1)/2

def meth_one(n):  # вариант через цикл
    num2 = 0
    for i in range(n):
        num2 += i+1
    return num2
# meth_one(20) 1000 loops, best of 5: 3.49 usec per loop
# meth_one(50) 1000 loops, best of 5: 7.74 usec per loop
# meth_one(250)1000 loops, best of 5: 40.5 usec per loop
# meth_one(500)1000 loops, best of 5: 93.2 usec per loop

def meth_two(n):  # вариант через список
    arr = [i for i in range(n+1)]
    num2 = sum(arr)
    return num2
# meth_two(20) 1000 loops, best of 5: 2.36 usec per loop
# meth_two(50) 1000 loops, best of 5: 3.54 usec per loop
# meth_two(250)1000 loops, best of 5: 13.6 usec per loop
# meth_two(500)1000 loops, best of 5: 30.7 usec per loop - лучшее быстродействие. Дополнительная память на список arr


def meth_three(n):  # вариант через рекурсию
    if n == 1:
        return n
    else:
        return n + meth_three(n-1)
# meth_three(20) 1000 loops, best of 5: 5.82 usec per loop
# meth_three(50) 1000 loops, best of 5: 15.4 usec per loop
# meth_three(250)1000 loops, best of 5: 85.2 usec per loop
# meth_three(500)1000 loops, best of 5: 189 usec per loop

'''
print(f'n(n+1)/2 = {num1}')
print(f'1+2+...+n = {meth_one(n)}')
print(f'1+2+...+n = {meth_two(n)}')
print(f'1+2+...+n = {meth_three(n)}')
'''