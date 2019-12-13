from fractions import Fraction
from numpy import sign
import math

def create_grid():
    with open('Day10/input','r') as f: input = f.read()
    grid = {}

    y = 0
    for line in input.split('\n'):
        x = 0
        for char in line:
            grid[(x,y)] = True if char == '#' else False
            x += 1
        y += 1
    return grid

def get_points_between(p1, p2):
    result = []
    (rise, run) = (0,0)
    (y_delta, x_delta) = (p2[1] - p1[1], p2[0] - p1[0])
    if x_delta == 0:
        (rise, run) = (1 * sign(y_delta), 0)
    else:
        f = Fraction(numerator = y_delta, denominator = x_delta)
        run = abs(f.denominator) * sign(x_delta)
        rise = abs(f.numerator) * sign(y_delta)        

    if (rise, run) == (y_delta, x_delta):
        # if the slope can't be reduced, there are no intermediate points.
        return result
    p = p1
    p = (p[0] + run, p[1] + rise)
    while p != p2:
        result.append(p)
        p = (p[0] + run, p[1] + rise)
        
    return result