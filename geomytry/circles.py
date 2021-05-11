from . import constants


def circumference(radius: float):
    c = (2 * radius) * constants.PI
    return float(round(c, 4))


def circumference_from_diameter(diameter: float):
    c = diameter * constants.PI
    return float(round(c, 4))


def radius(circumference: float):
    r = circumference / constants.TWOPI
    return float(round(r, 4))


def arc_length(angle: float, circumference: float):
    al = (angle / 360) * circumference
    return float(round(al, 4))
