from src.Triangle import Triangle

import pytest


name = "Trinity"

def test_triangle_perimeter():
    triangle = Triangle(name, 1, 2, 3)
    assert triangle.perimeter == 6

def test_triangle_area():
    triangle = Triangle(name, 7, 7, 3)
    assert triangle.area == 10.256095748383007

def test_triangle_add_area():
    triangle_first = Triangle(name, 2, 2, 3)
    triangle_second = Triangle(name, 2, 2, 3)
    assert triangle_first.add_area(triangle_second) == 3.968626966596886

def test_triangle_add_area_exception():
    triangle = Triangle(name, 1, 2, 3)
    with pytest.raises(ValueError):
        triangle.add_area(0)
