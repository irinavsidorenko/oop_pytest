from src.Rectangle import Rectangle


class Square(Rectangle):

    """ Calculate square area """
    @property
    def area(self):
        return self.side[0] * self.side[0]

    """ Calculate square perimeter """
    @property
    def perimeter(self):
        return self.side[0] * 4
