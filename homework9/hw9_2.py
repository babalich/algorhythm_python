# 2. Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter, namedtuple

class Node(namedtuple('Node', ['left', 'right'])):
    def move(self, code, acc):
        self.left.move(code, acc + '0')
        self.right.move(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def move(self, code, acc):
        code[self.char] = acc or '0'


def encode(text):
    h = []
    for char, freq in Counter(text).items():
        h.append((freq, len(h), Leaf(char)))
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, count1, left = heapq.heappop(h)
        freq2, count2, right = heapq.heappop(h)
        heapq.heappush(h,(freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.move(code, "")
    return code

text = 'beep boop beer!'

code = encode(text)
print(code)

enc_text = ''.join(code[i] for i in text)
print(enc_text)
