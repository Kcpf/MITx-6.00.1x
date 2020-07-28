# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:56:43 2020

@author: Fernando
"""

def bisection_search(L, e):
    """
    Input:
        L - list of elements
        e - element to find
    Output:
        boolean - if element is inside the list
    
    Assuming that L is sorted!
    Algorithm Complexity - O(n*log(n))
    """ 
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        mid_point = len(L) // 2
        if L[mid_point] > e:
            return bisection_search(L[:mid_point], e)
        else:
            return bisection_search(L[mid_point:], e)


def bisection_search2(L, e):
    """
    Input:
        L - list of elements
        e - element to find
    Output:
        boolean - if element is inside the list
    
    Assuming that L is sorted!
    Algorithm Complexity - O(log(n))
    """
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (high + low)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid-1)
        else:
            return bisect_search_helper(L, e, mid+1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)