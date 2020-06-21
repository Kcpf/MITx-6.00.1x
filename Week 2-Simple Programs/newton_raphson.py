# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:37:31 2020

@author: Fernando
"""

"""
General approximation algorithm to find roots of a polynomial in one variable

Want to find r such as p(r) = 0
For example, to find the square root of 24, find the root of p(x) = x**2 - 24

Newton showed that if g is an approximation to the root, then
    g - p(g)/p'(g)

is a better approximation; where p' is the derivative of p

"""

epsilon = 0.01
y = 24
guess = y/2
num_guesses = 0

while abs(guess**2 - y) >= epsilon:
    num_guesses += 1
    guess -= (guess ** 2 - y)/(2*guess)
    
print("numGuesse: {}".format(num_guesses))
print("Square root of {} is about {}".format(y, guess))


