#задание 2
def isCorrectRect(points):
    [(x1, y1), (x2, y2)] = points
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

#задание 3
class RectCorrectError(Exception):
    pass
def isCollisionRect(rectangles):
   rect1 = rectangles[0]
   x1,y1=rect1[0]
   x2,y2=rect1[1]
   if not (x1<x2 and y1<y2):
       raise RectCorrectError("1й треугольник некорректный") 
   rect2 = rectangles[1]
   x3,y3=rect2[0]
   x4,y4=rect2[1]
   if not (x3<x4 and y3<y4):
       raise RectCorrectError("2й треугольник некорректный") 
   if x1 >= x4 or x2 <= x3:
        return False

   if y1 >= y4 or y2 <= y3:
        return False

   return True

'''try:
    rect1 = []
    print("Введите координаты левого нижнего угла первого прямоугольника:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    rect1.append((x1, y1))

    print("Введите координаты правого верхнего угла первого прямоугольника:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    rect1.append((x2, y2))
except ValueError :
    print("Ошибка: вводите только числа. Попробуйте снова:")

try:
    rect2 = []
    print("Введите координаты левого нижнего угла второго прямоугольника:")
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))
    rect2.append((x3, y3))

    print("Введите координаты правого верхнего угла второго прямоугольника:")
    x4 = float(input("x4: "))
    y4 = float(input("y4: "))
    rect2.append((x4, y4))
except ValueError :
    print("Ошибка: вводите только числа. Попробуйте снова:")
rectangles=rect1,rect2
print(isCollisionRect(rectangles))'''