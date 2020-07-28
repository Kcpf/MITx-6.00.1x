# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 14:28:37 2020

@author: Fernando
"""


def bubble_sort(L):
    """
    Input: Unsorted List
    Output: Sorted List
    
    Complexity: O(n^2) where n is len(L)
    """
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j], L[j-1] = L[j-1], L[j]
    return L