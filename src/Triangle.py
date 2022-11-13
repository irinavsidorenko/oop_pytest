import math

from src.Figure import Figure


class Triangle(Figure):
    """ Calculate triangle perimeter """
    @property
    def perimeter(self):
        return self.side[0] + self.side[1] + self.side[2]

    """ Calculate triangle area """
    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return math.sqrt(half_perimeter * (half_perimeter - self.side[0]) * (half_perimeter - self.side[1]) * (
                    half_perimeter - self.side[2]))
