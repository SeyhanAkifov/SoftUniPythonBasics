import math

SQUARE = 'square'
RECTANGLE = 'rectangle'
CIRCLE = 'circle'
TRIANGLE = 'triangle'

def square_formula(a):
    return a * a

def rectangle_formula(a, b):
    return a * b

def circle_formula(a):
    return math.pi * (a * a)

def triangle_formula(a, b):
    return 1 / 2 * a * b


shape = input()

if shape == SQUARE:
    length = float(input())
    print("%.3f" % square_formula(length))
elif shape == RECTANGLE:
    a = float(input())
    b = float(input())
    print("%.3f" % rectangle_formula(a, b))
elif shape == CIRCLE:
    r = float(input())
    print("%.3f" % circle_formula(r))
elif shape == TRIANGLE:
    a = float(input())
    b = float(input())
    print("%.3f" % triangle_formula(a, b))





