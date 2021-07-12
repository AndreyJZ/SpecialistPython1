# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    
    if len(str(ticket_number)) == 6:
        sum1 = 0
        sum2 = 0
        ticket_number = str(ticket_number)
        len1 = (ticket_number[0:3])
        for n1 in len1:
            sum1 += int(n1)
        len2 = (ticket_number[3:6])
        for n2 in len2:
            sum2 += int(n2)   
    
        if sum1 == sum2:
            return  'Happy ticket'
    return 'Take another ticket'


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
