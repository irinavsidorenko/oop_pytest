class Figure:
    """ Figure class' attributes """
    def __init__(self, name, *sides):
        self.side = sides
        self.name = name

    """ Calculate figure area """
    def area(self):
        return 0

    """ Calculate figure perimeter """
    def perimeter(self):
        return 0

    """ Calculate figures' areas sum """
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Это не фигура!")
        return self.area + figure.area
