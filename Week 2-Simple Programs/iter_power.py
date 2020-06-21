# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:14:16 2020

@author: Fernando
"""


"""
Exercise: power iter

Write an iterative function iterPower(base, exp) that calculates the exponential 
base^exp by simply using successive multiplication. For example, iterPower(base, exp) 
should compute base^exp by multiplying base times itself exp times.
 
Write such a function below.

This function should take in two values - base can be a float or an integer; 
exp will be an integer ≥ 0. It should return one numerical value. 

Your code must be iterative - use of the ** operator is not allowed.
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    mult = base
    for i in range(exp-1):
        mult *= base
    return mult
        