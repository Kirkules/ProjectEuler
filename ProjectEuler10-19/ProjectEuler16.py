"""
Created by Kirk Anthony Boyer
7/9/2012
Solution to Project Euler Problem 16
	Problem:	What is the sum of the digits of the number 2^1000?
	Idea:		Brute force; straightforward. We are lucky that python's math
				already handles large-sized numbers.
"""
import math

def sumDigits(n):
	sum = 0
	for digit in n:
		sum += digit
	return sum



num = int(math.pow(2,1000))
num = str(num)
num.split()
num = list(num)
for i in range(len(num)):
	num[i] = int(num[i])
print "sum of digits in 2^1000 is ", sumDigits(num)