import math

from src.Figure import Figure


class Circle(Figure):

    """ Calculate circle area """
    @property
    def area(self):
        return math.pi * self.side[0] * self.side[0]

    """ Calculate round """
    @property
    def perimeter(self):
        return 2 * math.pi * self.side[0]
