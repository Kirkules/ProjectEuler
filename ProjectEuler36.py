"""
Created by Kirk Anthony Boyer
7/13/2012
Solution to Project Euler problem 36
	Problem:	What is the sum of the numbers, below 1million, which are palindromes both
				in base 10 and base 2l
	Idea:		
"""
import time
from sys import stdout
import math

tic = time.time()

"""
isPal(s)
	Takes a string as parameter and returns True if it is a palindrome, False if it is not.

example:
	input: "Hello"
	output: False
	
	input: "Fasaf"
	output: False
	
	input: "fasaf"
	output: True
"""
def isPal(s):
	s = list(s)
	n = len(s)
	k = int(n/2)
	for i in range(k):
		if not s[i]==s[n-i-1]:
			return False
	return True
	
def binaryString(n):
	s = ''
	while n != 0:
		if n%2:
			s = '1'+s
		else:
			s = '0'+s
		n /= 2
	return s


total = 0
skipduplicate = False
even = True
for i in range(1,1000000):
	even = not even
	if even:
		skipduplicate = False
		continue
	if skipduplicate:
		skipduplicate = False
		continue
	if isPal(str(i)):
		if isPal(binaryString(i)):
			total += i
			skipduplicate = True
			print i, binaryString(i)
	

print "total is", total
print "took", time.time()-tic, "seconds."