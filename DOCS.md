# Geomytry

## Library for working with geometry

install by running ```pip install geomytry``` or if on *NIX systems run ```pip3 install geomytry```

### The circles modules

The circumference function

```python
from geomytry import circles
circles.circumference(10) # OUTPUTS 62.8
circles.circumference_from_diameter(20) # OUTPUTS 62.8
```

- circles.circumference
  - Takes only 1 argument
    - The radius of the circle
- circles.circumference_from_diameter
  - Takes 1 argument
    - Diameter of the circle

The radius function

```python
from geomytry import circles
circles.radius(10) # OUTPUTS 3.1847
```

- Finds the radius of a circle
  - Takes one parameter
    - The circumference of the circle

The arc length function

```python
from geomytry import circles
circles.arc_length(30, 100) # OUTPUT 8.333
```

- Finds the length of an arc using the given angle and circumference
  - Takes two parameters
    - measurement of the angle inside the circle
    - circumference of the circle
