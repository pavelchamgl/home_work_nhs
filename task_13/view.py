from triangle import square_triangle, perimetr_triangle
from circle import square_circle, perimetr_circle
from rectangle import square_rectangle, perimetr_rectangle


def print_triangle(square_trinagle, perimetr_triangle):
    return {"triangle": {"square": square_trinagle, "perimetr": perimetr_triangle}}

print(print_triangle(square_triangle(5,6,7,5.6), perimetr_triangle(5,6,7)))

def print_circle(square_circle, perimetr_circle):
    return {"circle": {"square": square_circle, "perimetr": perimetr_circle}}

print(print_circle(square_circle(5.5), perimetr_circle(10)))

def print_rectangle(square_rectangle, perimetr_rectangle):
    return {"rectangle": {"square": square_rectangle, "perimetr": perimetr_rectangle}}

print(print_rectangle(square_rectangle(3.8, 5.2),perimetr_rectangle(3.8, 5.2)))