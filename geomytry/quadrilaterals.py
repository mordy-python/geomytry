from . import constants


def area(side_length):
  return side_length * side_length

def surface_area_rect(length, width, height):
	bottom_top = 2*(length*width)
	left_right = 2*(width*height)
	fron_back = 2*(length*height)
	total_area = bottom_top+left_right+fron_back
	return float(round(total_area,4))
def surface_area_cube(side_length):
	total_area = 2*(side_length**2)
	return float(round(total_area,4))
def volume_cube(side_length):
	total_vol = side_length**3
	return float(round(total_vol, 4))

def perimiter(side_length):
  return side_length * 4
def volume_rect(length, width, height):
	total_vol = length*width*height
	return float(round(total_vol, 4))
