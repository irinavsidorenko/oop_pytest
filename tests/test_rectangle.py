from src.Rectangle import Rectangle

import pytest


name = "Five angles"

def test_rectangle_perimeter():
    rectangle = Rectangle(name, 1, 2)
    assert rectangle.perimeter == 2 * (1 + 2)

def test_rectangle_area():
    rectangle = Rectangle(name, 1, 2)
    assert rectangle.area == 2

def test_rectangle_add_area():
    rectangle_first = Rectangle(name, 1, 2)
    rectangle_second = Rectangle(name, 3, 4)
    assert rectangle_first.add_area(rectangle_second) == 14

def test_rectangle_add_area_exception():
    rectangle = Rectangle(name, 1, 2)
    with pytest.raises(ValueError):
        rectangle.add_area(0)
