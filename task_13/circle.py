from math import pi


def perimetr_circle(diametr: float) -> float:
    return round(diametr*pi, 2)

def square_circle(radius: float) -> float:
    return round(pi*(radius**2), 2)
