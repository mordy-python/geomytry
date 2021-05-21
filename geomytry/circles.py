from . import constants


def circumference(radius: float):
    c = (2 * radius) * constants.PI
    return float(round(c, 4))


def area(radius: float):
    a = constants.PI * (radius ** 2)
    return float(round(a, 4))


def circumference_from_diameter(diameter: float):
    c = diameter * constants.PI
    return float(round(c, 4))


def radius(circumference: float):
    r = circumference / constants.TWO_PI
    return float(round(r, 4))


def shaded_area(big_radius: float, small_radius: float):
    area1 = area(big_radius)
    area2 = area(small_radius)
    inside_area = area1 - area2
    return float(round(inside_area, 4))


def arc_length(angle: float, circumference: float):
    al = (angle / 360) * circumference
    return float(round(al, 4))


def arc_area(angle: float, area_of_arc: float):
    area = (angle / 360) * area_of_arc
    return float(round(area, 4))
