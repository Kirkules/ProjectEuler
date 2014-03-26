"""
Created by Kirk Anthony Boyer
7/5/2012
Quick Solution to Project Euler Problem 1
"""
i = 3
sum = 0
while i < 1000:
	if (i%3 == 0) or (i%5 == 0):
		sum += i
		print i
	i+= 1

print sum