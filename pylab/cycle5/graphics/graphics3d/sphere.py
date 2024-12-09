def area(radius):
    from math import pi
    return 4 * pi * radius * radius

def perimeter(radius):  # Perimeter doesn't apply to a sphere; return the circumference of a great circle
    from math import pi
    return 2 * pi * radius
