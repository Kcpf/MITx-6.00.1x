# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:16:51 2020

@author: Fernando
"""
import random

def bogo_sort(L):
    """
    Input: Unsorted List
    Output: Sorted List
    
    best case: O(n) where n is len(L) to check if sorted
    worst case: it is unbounded if really unlucky
    """
    while L != sorted(L):
        random.shuffle(L)
    return L