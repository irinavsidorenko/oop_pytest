from src.Triangle import Triangle

import pytest


name = "Trinity"

def test_triangle_perimeter():
    triangle = Triangle(name, a=1, b=2, c=3)
    assert triangle.perimeter == 6

def test_triangle_area():
    triangle = Triangle(name, a=7, b=7, c=3)
    assert triangle.area == 10.256095748383007

def test_triangle_add_area():
    triangle_first = Triangle(name, a=2, b=2, c=3)
    triangle_second = Triangle(name, a=2, b=2, c=3)
    assert triangle_first.add_area(triangle_second) == 3.968626966596886

def test_triangle_add_area_exception():
    triangle = Triangle(name, a=1, b=2, c=3)
    with pytest.raises(ValueError):
        triangle.add_area(0)

@pytest.mark.parametrize("value", [-1, 0, 33])
def test_triangle_create_exception_side_a(value):
    with pytest.raises(ValueError):
        Triangle(name, a=value, b=1, c=2)

@pytest.mark.parametrize("value", [-1, 0, 33])
def test_triangle_create_exception_side_b(value):
    with pytest.raises(ValueError):
        Triangle(name, a=1, b=value, c=2)

@pytest.mark.parametrize("value", [-1, 0, 33])
def test_triangle_create_exception_side_c(value):
    with pytest.raises(ValueError):
        Triangle(name, a=1, b=2, c=value)
