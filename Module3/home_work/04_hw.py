# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

import random
numbers1 = []
numbers2 = []
n = int(input('Введите число элементов: '))
sm = 0

for el_1 in range(n):
    numbers1.append(random.randint(-100, 100))
for el_2 in numbers1:
    if el_2 > 0 and el_2**0.5*10 % 10 == 0:
        numbers2.append(el_2)
        
print(numbers1)
print()
print(numbers2)
