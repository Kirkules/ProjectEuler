"""
Created by Kirk Anthony Boyer
7/10/2012
Solution to Project Euler Problem 25
	Problem:	How many digits does the 1000th number in the Fibonacci series have?
	Idea:		Brute force, calculate subsequent terms and count digits.
				Very quick.
"""

a = 1
b = 1
c = 2
n = 3 #the index of c
while len(str(c)) < 1000:
	n += 1
	a = b
	b = c
	c = a+b
print n