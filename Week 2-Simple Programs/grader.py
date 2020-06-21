# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:39:19 2020

@author: Fernando
"""


"""
Grader

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: (0.25∗n∗s^2)/tan(π/n)

The perimeter of a polygon is: length of the boundary of the polygon

Write a function called polysum that takes 2 arguments, n and s. This function 
should sum the area and square of the perimeter of the regular polygon. The 
function returns the sum, rounded to 4 decimal places.
"""

from math import pi, tan

def polysum(n, s):
    """
    n: Number of sides
    s: Length of each side
    
    returns: sum of the area and square of the perimeter of the regular polygon
    """
    area = (0.25*n*(s**2))/tan(pi/n) # Calculate the polygon area
    square_perimeter = (n*s)**2 # Calculate the square of the polygon perimeter
    
    # Sum the area and square perimeter and round it to 4 decimal places
    return round(area + square_perimeter, 4) 