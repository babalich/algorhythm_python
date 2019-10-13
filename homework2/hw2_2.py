# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input('Введите любое натуральное число'))
even = 0
odd = 0

while a > 0:
    num = a % 10
    a //= 10
    if num % 2 == 0 or num == 0:
        even += 1
    else:
        odd += 1

print(f'Четных цифр {even}, нечетных {odd}')