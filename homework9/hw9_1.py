# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
# задача считается не решённой.
import hashlib


text = 'im a banana'

subs_set = set()

for i in range(len(text)):
    for j in range(len(text)-1 if i == 0 else len(text), i, -1):
        subs_set.add(hash(text[i:j]))

print("Количество различных подстрок в этой строке:", len(subs_set))