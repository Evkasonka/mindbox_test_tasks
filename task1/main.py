# Импортируем необходимые библиотеки
import math


# Определяем класс "Shape"
class Shape:
    def area(self):
        pass

# Определяем класс "Circle", который наследуется от класса "Shape"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Метод для вычисления площади круга
    def area(self):
        return math.pi * (self.radius ** 2)

# Определяем класс "Triangle", который наследуется от класса "Shape"
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Метод для вычисления площади треугольника
    def area(self):
        semi_perimeter = (self.a + self.b + self.c) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter - self.c))

    # Метод для проверки, является ли треугольник прямоугольным
    def is_rectangular(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
