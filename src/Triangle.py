import math

from src.Figure import Figure


class Triangle(Figure):
    """Override Triangle class constructor and add condition for triangle creation"""
    def __init__(self, name, a, b, c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
        if self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
            raise ValueError("Треугольник с такими сторонами создать невозможно!")

    """ Calculate triangle perimeter """
    @property
    def perimeter(self):
        return self.a + self.b + self.c

    """ Calculate triangle area """
    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (
                    half_perimeter - self.c))
