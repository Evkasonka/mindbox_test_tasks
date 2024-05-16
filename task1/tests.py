import unittest
from main import Circle, Triangle


# Определяем класс для тестирования
class TestShapes(unittest.TestCase):
    # Тест для проверки площади круга
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    # Тест для проверки площади треугольника
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    # Тест для проверки, является ли треугольник прямоугольным
    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_rectangular())


# Запускаем тесты
if __name__ == '__main__':
    unittest.main()
