# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
n = int(input('Введите число элементов: '))
sm = 0

for el in range(n):
    numbers.append(random.randint(-100, 100))
for el in numbers:
    if el > 0 and el % 2 == 0:
        sm += el
print(sm)
