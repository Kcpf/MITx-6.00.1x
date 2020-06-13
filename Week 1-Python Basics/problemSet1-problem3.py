"""
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur 
in alphabetical order. For example, if s = 'azcbobobegghakl', then your program 
should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
"""

longest = ""
for j in range(0, len(s)):
    for i in range(0, len(s)):
        if s[j:i+1] == "".join(sorted(s[j:i+1])):
            if len(s[j:i+1]) > len(longest):
                longest = s[j:i+1]

print(longest)