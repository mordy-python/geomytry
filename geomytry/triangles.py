from . import constants
from math import sqrt

def find_side_length_eq(side_length):
    side = side_length/3
    return round(float(side), 4)

def pythagorean_theorem(a,b):
    a = a**2
    b = b**2
    c_squared = sqrt(a+b)
    return float(round(c_squared, 4))