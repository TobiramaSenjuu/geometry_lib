# -*- coding: utf-8 -*-


import math


# ������� ������� ���������� ������� �����, ������������ ������� S = pi * r^2
def circle_area(radius):

  return math.pi * radius ** 2

# ������� ���������� ������� ������������ �� ������� ������

def triangle_area(a, b ,c):

  semiperimeter = (a + b + c) / 2

  area = math.sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c))

  return area

# ������ �������������

# print(circle_area(5))

# print(triangle_area(14, 15, 13))
