#задание 2
def isCorrectRect(points):
    [(x1, y1), (x2, y2)] = points
    return x1 < x2 and y1 < y2

#Пример использования функции
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
    print("Ошибка: вводите только числа. Попробуйте снова")
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

#Пример использования функции
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
    print("Ошибка: вводите только числа. Попробуйте снова")

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
    print("Ошибка: вводите только числа. Попробуйте снова")
rectangles=rect1,rect2
print(isCollisionRect(rectangles))'''

#задание 5
class RectCorrectError(Exception):
    pass
def intersectionAreaMultiRect(rectangles):
      if not rectangles:
        return 0
    
      if len(rectangles) == 1:
        rect = rectangles[0]
        x1, y1 = rect[0]
        x2, y2 = rect[1]
        return (x2 - x1) * (y2 - y1)
    
      for i, rect in enumerate(rectangles, 1):
        x1, y1 = rect[0]
        x2, y2 = rect[1]
        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError(f"{i} прямоугольник не существует")
    
      current_x1, current_y1 = rectangles[0][0]
      current_x2, current_y2 = rectangles[0][1]
    

      for i in range(1, len(rectangles)):
        x1, y1 = rectangles[i][0]
        x2, y2 = rectangles[i][1]
        
    
        new_x1 = max(current_x1, x1)
        new_x2 = min(current_x2, x2)
        new_y1 = max(current_y1, y1)
        new_y2 = min(current_y2, y2)

        if new_x1 >= new_x2 or new_y1 >= new_y2:
            return 0  
        
        current_x1, current_y1 = new_x1, new_y1
        current_x2, current_y_up = new_x2, new_y2
    
      width = current_x2 - current_x1
      height = current_y_up - current_y1
      return width * height

#Пример использования функции
'''rectangles = []
try:
        
        for i in range(4):
            print(f"\nПрямоугольник {i+1}:")
            left_down_x = float(input("  Введите координату x левого нижнего угла: "))
            left_down_y = float(input("  Введите координату y левого нижнего угла: "))
            right_up_x = float(input("  Введите координату x правого верхнего угла: "))
            right_up_y = float(input("  Введите координату y правого верхнего угла: "))
            
            rectangles.append([(left_down_x, left_down_y), (right_up_x, right_up_y)])
        
        area = intersectionAreaMultiRect(rectangles)
        
        if area > 0:
            print(f"Площадь пересечения всех прямоугольников: {area}")
        else:
            print(f"Прямоугольники не имеют общего пересечения")
except ValueError:
    print("Ошибка: вводите только числа. Попробуйте снова")'''