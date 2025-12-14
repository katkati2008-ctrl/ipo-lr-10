#задание 2
def isCorrectRect(points):
    (x1, y1), (x2, y2) = points
    return x1 < x2 and y1 < y2

'''points = []
try:
    points = []
    print("Введите координаты левого нижнего угла:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    points.append((x1, y1))

    print("Введите координаты правого верхнего угла:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    points.append((x2, y2))
except ValueError :
    print("Ошибка: вводите только числа. Попробуйте снова:")
print(isCorrectRect(points))'''