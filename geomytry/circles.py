import constants

def circumference(radius):
    c = (2*radius)*constants.PI
    return c
def circumference_diameter(diameter):
    c = diameter * constants.PI
def radius(circumference):
    r = circumference/constants.TWOPI
    return r
def arc_length(angle, circumference):
    al = (angle/360)*circumference
    return al