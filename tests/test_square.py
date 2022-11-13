from src.Square import Square

import pytest


name = "Just square"

def test_square_perimeter():
    square = Square(name, 3)
    assert square.perimeter == 4 * 3

def test_square_area():
    square = Square(name, 3)
    assert square.area == 9

def test_square_add_area():
    square_first = Square(name, 3)
    square_second = Square(name, 4)
    assert square_first.add_area(square_second) == 25

def test_square_add_area_exception():
    square = Square(name, 3)
    with pytest.raises(ValueError):
        square.add_area("some string932489842")
