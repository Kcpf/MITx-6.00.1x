# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:44:23 2020

@author: Fernando
"""
def merge(left, right):
    """
    Suport function for merge sort
    
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def merge_sort(L):
    """
    Input: Unsorted List
    Output: Sorted List
    
    Complexity: O(n*log(n)) where n is len(L)
    """
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])  
        right = merge_sort(L[middle:])
        return merge(left, right)
    

    
    
