"""
Created by Kirk Anthony Boyer
7/10/2012
Solution to Project Euler Problem 30
	Problem:	Find the sum of all numbers equal to the sum of the fifth powers of their 
				digits.
	Idea:		The largest value of a digit to the fifth power is 9^5=59049
				7(9^5) is less than 9,999,999, and 6(9^5) is 354294, which has 6
				digits, but is clearly not 6 9's. Either way, 354294 is a clear
				upper bound.
				
				First let's see how fast brute force checking is, up to 354294.
						(took ~6 seconds)
"""
import math
import time
from sys import stdout
tic = time.time()

def intToDigitArray(n):
	digits = []
	while n:
		digits.append(n%10)
		n /= 10
	return digits

sum = 0
digits = range(8) #this is how big the digit array can get
for i in range(13,354294):
	stdout.write("\r\x1b[K"+str(i))
	stdout.flush()
	digits = intToDigitArray(i)
	s = 0
	for d in digits:
		s+= math.pow(d,5)
	if i==s:
		sum += i

print "Total sum is", sum
print "Took", time.time()-tic, "seconds."