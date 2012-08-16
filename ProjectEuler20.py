"""
Created by Kirk Anthony Boyer
7/9/2012
Solution to Project Euler problem 20
	Problem: 	Find the sum of the digits in 100!
	Idea:		Take advantage of python's large-number handling, and use brute force.
				Similar implementation to the solution to problem 16.
"""
import math

def sumDigits(n):
	sum = 0
	for digit in n:
		sum += digit
	return sum

def factorial(n):
	prod = 1
	for i in range(n):
		prod *= (1+i)
	return prod



num = factorial(100)
num = str(num)
num.split()
num = list(num)
for i in range(len(num)):
	num[i] = int(num[i])
print "sum of digits in 100! is ", sumDigits(num)
