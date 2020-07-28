# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:44:35 2020

@author: Fernando
"""

def linear_search(L, e):
    """
    Input:
        L - list of elements
        e - element to find
    Output:
        boolean - if element is inside the list
    
    Assuming that L is NOT sorted
    Algorithm Complexity - O(n)
    """
    found = False
    for i in L:
        if e == i:
            found = True
    return found