from src.Figure import Figure


class Rectangle(Figure):

    """ Calculate rectangle are """
    @property
    def area(self):
        return self.side[0] * self.side[1]

    """ Calculate rectangle perimeter """
    @property
    def perimeter(self):
        return (self.side[0] + self.side[1]) * 2
