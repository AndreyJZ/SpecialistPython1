# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

m = int(input())

if m == 12 or 1 <= m <= 2:
    print('winter')
elif 3 <= m <= 5:
    print('spring')
elif 6 <= m <= 8:
    print('summer')
elif 9 <= m <= 11:
    print('autumn')
