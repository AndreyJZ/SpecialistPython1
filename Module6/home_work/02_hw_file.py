# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения
sum = 0
list1 = []

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

with open("info.txt", "r") as f:
    for line in f:
        list1.append(line.rstrip())
    for el in list1:
        if is_number(el):
            sum += int(el)
    print(sum)
