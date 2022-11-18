from src.Circle import Circle

import math

import pytest


name = "Circus"

def test_circle_perimeter():
    circle = Circle(name, 4)
    assert circle.perimeter == 2 * math.pi * 4

def test_circle_area():
    circle = Circle(name, 4)
    assert circle.area == math.pi * (4 * 4)

def test_circle_add_area():
    circle_first = Circle(name, 5)
    circle_second = Circle(name, 8)
    assert circle_first.add_area(circle_second) == math.pi * (5 * 5) + math.pi * (8 * 8)

def test_circle_add_area_exception():
    circle_first = Circle(name, 5)
    with pytest.raises(ValueError):
        circle_first.add_area("some_string")
