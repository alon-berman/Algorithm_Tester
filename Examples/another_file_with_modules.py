"""
This file was made in order to test support for modules which aren't located particularly in this project.
"""
import numpy as np


def p2(num):
    out = 0
    for i in range(num):
        out += i
    return out


def get_radius_from_perimeter(perimeter):
    return perimeter / 2*np.pi
