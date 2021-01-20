"""
Compute volumes
    Return value (NOT print)
    Cube formula
        a^3
    Pyramid formula
        1/3 * b^2 * h
    Ellipsoid
        4/3 * pi * r1 * r2 * r3

"""

# Justin Yan #
# jyan388 #
# 251150279 #
# Section 001 #

import math


# compute cube volume #
def cube_volume_formula(a):
    cube_volume = a ** 3
    return cube_volume


# compute pyramid volume #
def pyramid_volume_formula(b, h):
    pyramid_volume = (1 / 3) * (b ** 2) * h
    return pyramid_volume


# compute ellipsoid volume #
def ellipsoid_volume_formula(r1, r2, r3):
    ellipsoid_volume = (4 / 3) * math.pi * r1 * r2 * r3
    return ellipsoid_volume


