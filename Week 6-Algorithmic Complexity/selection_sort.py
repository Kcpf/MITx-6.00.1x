# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:59:05 2020

@author: Fernando
"""


def selection_sort(L):
    """
    Input: Unsorted List
    Output: Sorted List
    
    Complexity: O(n^2) where n is len(L)
    """
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
    return L