# -*- coding: utf-8 -*-


import math


# ������� ������� ���������� ������� �����, ������������ ������� S = pi * r^2:

def circle_area(radius):

  area = math.pi * radius ** 2

  return area

# ������� ���������� ������� ������������ 

def triangle_area(a, b ,c):
  
  # �������� �������� � ������� � ����������� ���������� ��� ���������� �������� �� ��������������� ������������:

  a2 = a ** 2
  b2 = b ** 2
  c2 = c ** 2

  # �������� ������������� �� �����������:

  if (c2 == a2 + b2) or (a2 == c2 - b2) or (b2 == c2 - a2):

    print("����������� �������������.")

    area = ((a * b)/2)


    return area
  
  else:

    print("����������� �� �������������.")

    # ��������� ������� �� ���� �������� �� ������� ������:

    semiperimeter = (a + b + c) / 2

    area = math.sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))


    return area

# ������ ������������� ����������:

# import geometry

# area_of_triangle = geometry.triangle_area(3, 4, 5)

# area_of_circle = geometry.circle_area(8)
