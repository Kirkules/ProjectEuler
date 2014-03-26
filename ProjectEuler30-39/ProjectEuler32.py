"""
Created by Kirk Anthony Boyer
7/12/2012
Solution to Project Euler problem 32
	Problem:	Find the sum of all products p with an identity a * b = p is pandigital.
	Idea:		The first thing to notice is that if the identity is pandigital, then
				there are a total of 9 digits used. 
				
				-p can clearly not have 1, 2, or 3 digits, for otherwise the terms a and b
				 in the product identity would have too few digits to make a pandigital
				 identity.
				-p could have 4 digits, and if so, (without loss of generality), a could 
				 have 1 or 2 digits and b would have 4 or 3 digits (respectively). 
				-p could not have 5 digits, for if it did, it would have to be a product
				 of two numbers whose total digit count was 4. For the same reason p can
				 not have more than 5 digits
				 
				 So, in fact, p must have 4 digits. Naively, there are 9 choose 4 = 126
				 numbers that could be p. So a brute force approach would first find
				 a list of these possibilities (4-digit numbers with no repeated digits),
				 and then iterate through a list of factors of each possibility to see if
				 they create a pan-digital result.
				
				
"""
import string
import time
tic = time.time()

def isPandigital(s):
	history = ''
	for digit in s:
		if digit in history:
			return False
		if digit == '0':#arbitrary definition of pandigital does not include digit 0
			return False
		history += digit
	return True

#create a list of 1-, 2-, 3-, and 4-digit numbers with no repeated digit
#to optimize even more, combine this step and the checking-for-pandigitalness steps into 1
ones = range(1,9+1)
twos = []
threes = []
fours = []
for i in range(12,98+1):
	if isPandigital(str(i)):
		twos.append(i)
for i in range(123, 987+1):
	if isPandigital(str(i)):
		threes.append(i)
for i in range(1234,9876+1):
	if isPandigital(str(i)):
		fours.append(i)

s = 0
#iterate through the possible identity constituents and if they are, together, pandigital,
#  record them in the sum


history = [] #since we expect so few results (on the order of 10), storing all of these
			 #has a negligible effect on the performance of the program
for a in threes:
	for b in twos:
		if isPandigital(str(a)+str(b)+str(a*b)) and (a*b) not in history:
			s += a*b
			history.append(a*b)

for a in fours:
	for b in ones:
		if isPandigital(str(a)+str(b)+str(a*b)) and (a*b) not in history:
			s += a*b
			history.append(a*b)
			
print "Total sum is:", s
print "Took ", time.time() - tic, "seconds."

