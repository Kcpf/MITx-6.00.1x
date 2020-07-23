# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:22:41 2020

@author: Fernando
"""


# =============================================================================
# Exercise: genPrimes
# 
# Write a generator, genPrimes, that returns the sequence of prime numbers on 
# successive calls to its next() method: 2, 3, 5, 7, 11, ...
# 
# Hints
# Ideas about the problem
# Have the generator keep a list of the primes it's generated. A candidate number 
# x is prime if (x % p) != 0 for all earlier primes p.
# 
# =============================================================================

def genPrimes():
    yield 2
    primes = [2]
    num = 3
    while True:
        broken = False
        for each in primes:
            if (num % each) == 0:
                broken = True
                break
        if not broken:
            yield num
            primes.append(num)
        num += 1

n = 0
for i in genPrimes():
    if n == 10:
        break
    print(i)
    n +=1