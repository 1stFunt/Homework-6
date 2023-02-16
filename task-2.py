# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
list_1 = list([randint(-10, 11) for i in range(20)])
print(list_1)
min = int(input())
max = int(input())
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')