"""
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 

Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if 
s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

cont = 0

for each in s:
    if each == "a" or each == "e" or each == "i" or each == "o" or each == "u":
        cont += 1

print("Number of vowels: {}".format(cont))