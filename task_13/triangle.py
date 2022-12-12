
def perimetr_triangle(side_a: float, side_b: float, side_c: float) -> float:
    return round(side_a + side_b + side_c, 2)

def square_triangle(side_a: float, side_b: float, side_c: float, radius: float) -> float:
    return round((side_c*side_a*side_b) / (4*radius), 2)
