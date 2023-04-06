import unittest
from task_1 import *


class TriangleCheckTest(unittest.TestCase):
    def test_triangle_check(self):
        self.assertEqual(triangle_check(9, 4, 6), "Треугольник разносторонний")
        self.assertEqual(triangle_check(5, 5, 8), "Треугольник равнобедренный")
        self.assertEqual(triangle_check(5, 5, 5), "Треугольник равносторонний")
        self.assertEqual(triangle_check(4, 5, 10), "Треугольник не существует")

if __name__ == "__main__":
    unittest.main()
