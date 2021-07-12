# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    copy_number = number
    rev_number = 0
    while number:
        digit = number % 10
        number = number // 10
        rev_number = rev_number * 10 + digit
    return copy_number == rev_number

def quantity_palindrome(a, b):
    count = 0
    for digit2 in range(a, b):
        digit2 += 1
        if palindrome(digit2):
            count += 1
    return count

print(quantity_palindrome(1, 20))
