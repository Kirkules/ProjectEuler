"""
Created by Kirk Anthony Boyer
7/13/2012
Solution to Project Euler Problem 37
	Problem: 	The number 3797 has an interesting property. Being prime itself, it is 
				possible to continuously remove digits from left to right, and remain 
				prime at each stage: 3797, 797, 97, and 7. Similarly we can work from 
				right to left: 3797, 379, 37, and 3.

				Find the sum of the only eleven primes that are both truncatable from left
				to right and right to left.

				NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
				
				(I will also call these strippable primes)
				
	Idea: 		Assuming the hints are correct, we have been given 5 of the 11 such primes
				already: 3797, 797, 97, 379, and 37. 
				
				Interestingly, not all the strippable primes yield more strippable primes
				in this way (the only example being the largest strippable prime, 
				739397, which doesn't yield more because of the 9's in its digits
				causing trouble).
"""
import time
import math
from sys import stdout

tic = time.time()
primes = [2,3,5]
def isPrime(n):
	s = int(math.sqrt(n))
	for p in primes:
		if p > s:
			break
		if n%p == 0:
			return False
	return True
	

i = 7
while primes[-1] < 1000000:
	if isPrime(i):
		primes.append(i)
	i+=4
	if (i > 1000000):
		break
	if isPrime(i):
		primes.append(i)
	i+=2
	
sprimes = set()
"""
sprimes.add(3797)
sprimes.add(797)
sprimes.add(97)
sprimes.add(379)
sprimes.add(37)
"""

def stripLeft(n):
	return n%(10**(len(str(n))-1))
	
def stripRight(n):
	return n/10
	
def rightStrippable(n):
	k = n
	while k != 0:
		if k not in primes:
			return False
		k = stripRight(k)
	return True

def leftStrippable(n):
	k = n
	while k != 0:
		if k not in primes:
			return False
		k = stripLeft(k)
	return True
		

for p in primes:
	if p < 10:
		continue
	
	stdout.write('\r\x1b[K'+'Current prime is: '+str(p)+'. Number of strippable primes:'+str(len(sprimes)))
	stdout.flush()
	if leftStrippable(p) and rightStrippable(p):
		sprimes.add(p)

	
	
sprimes = list(sprimes)
sprimes.sort()
print
print "the strippable primes:", sprimes
print "their sum is:", sum(sprimes), "and there are", len(sprimes), "of them."
toc = time.time() - tic
print "time: ", toc