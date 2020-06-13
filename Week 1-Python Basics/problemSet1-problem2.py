"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

cont = 0
l = []

for i in range(len(s)):
    l.append(s.count("bob", i, i+3))

print(sum(l))