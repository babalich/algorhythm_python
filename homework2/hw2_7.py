# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input('Введите натуральное число'))

num1 = n*(n+1)/2
num2 = 0

for i in range(n):
    num2 += i+1

print(f'n(n+1)/2 = {num1}')
print(f'1+2+...+n = {num2}')