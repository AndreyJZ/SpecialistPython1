# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):

    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return d

coordinates = ((81, 5), (41, 3), (81, 7))

A = coordinates[0]
B = coordinates[1]
C = coordinates[2]

AB = distance(*A, *B)
BC = distance(*B, *C)
AC = distance(*A, *C)

# print(AB, BC, AC, sep='\n')

if AB <= AC and AB <= BC:
    print("Самый короткий отрезок: AB")  # Выводим название отрезка, например “АС”.
elif BC <= AB and BC <= AC:
    print("Самый короткий отрезок: BC")
else:
    print("Самый короткий отрезок: AC")
