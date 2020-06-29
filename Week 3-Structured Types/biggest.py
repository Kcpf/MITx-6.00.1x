# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:22:21 2020

@author: Fernando
"""


"""
Exercise: biggest

Consider the following sequence of expressions:
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

We want to write some simple procedures that work on dictionaries to return information.
This time, write a procedure, called biggest, which returns the key corresponding 
to the entry with the largest number of values associated with it. If there is 
more than one such entry, return any one of the matching keys.

>>> biggest(animals)
'd'

If there are no values in the dictionary, biggest should return None.
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest_count = 0
    biggest_name = ""
    for each in aDict:
        if len(aDict[each]) > biggest_count:
            biggest_count = len(aDict[each])
            biggest_name = each
    return biggest_name
