import math


# Создаем функцию вычисления площади круга, классическая формула S = pi * r^2:

def circle_area(radius):

  area = math.pi * radius ** 2

  return area

# Функция вычисления площади треугольника 

def triangle_area(a, b ,c):
  
  # Возводим значения в квадрат и присваиваем переменной для дальнейшей проверки на прямоугольность треугольника:

  a2 = a ** 2
  b2 = b ** 2
  c2 = c ** 2

  # Проверям прямоугольный ли треугольник:

  if (c2 == a2 + b2) or (a2 == c2 - b2) or (b2 == c2 - a2):

    print("Треугольник прямоугольный.")

    area = ((a * b)/2)


    return area
  
  else:

    print("Треугольник НЕ прямоугольный.")

    # Вычисляем площадь по трем сторонам по формуле Герона:

    semiperimeter = (a + b + c) / 2

    area = math.sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))


    return area

# Пример использования библиотеки:

# import geometry

# area_of_triangle = geometry.triangle_area(3, 4, 5)

# area_of_circle = geometry.circle_area(8)
