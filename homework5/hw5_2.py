# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.

from collections import deque

def hex_to_cel(value):
    val1 = deque(list(value))
    val1.reverse()
    result = 0
    for i in range(len(val1)):
        if val1[i] in hex_table:
            val1[i] = hex_table[val1[i]]
        result += int(val1[i]) * (16 ** i)
    return result

def dec_to_hex(value):
    value = int(value)
    result = deque()
    while value >= 16:
        digit = value % 16
        if digit in hex_table.values():
            digit = str([key for key, val in hex_table.items() if val == digit][0])
        result.append(str(digit))
        value //= 16
    else:
        if value in hex_table.values():
            value = str([key for key, val in hex_table.items() if val == value][0])
        result.append(str(value))
    result.reverse()
    return ''.join(result)

hex_table = {'A': 10,
             'B': 11,
             'C': 12,
             'D': 13,
             'E': 14,
             'F': 15}

input1 = 'A2'
input2 = 'C4F'

number1 = hex_to_cel(input1)
number2 = hex_to_cel(input2)

sum = number1 + number2
prod = number1 * number2

print(f'Сумма равна: {dec_to_hex(sum)}')
print(f'Произведение равно: {dec_to_hex(prod)}')


