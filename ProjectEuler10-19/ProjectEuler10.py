"""
Created by Kirk Anthony Boyer
7/5/2012
Solution to Project Euler Problem 10
	Problem: Find the sum of the primes below 2,000,000
	Idea: First: brute force; find the primes and then sum them
			takes 7 seconds -- too long. Not sure how to optimize more at the moment
			
"""
import time
import math
tic = time.time()
primes = [2,3,5]
t = sum(primes)
def isPrime(n):
	s = int(math.sqrt(n))
	for p in primes:
		if p > s:
			break
		if n%p == 0:
			return False
	return True
	
i = 7
while primes[-1] < 2000000:
	if isPrime(i):
		primes.append(i)
		t+= i
	i+=4
	if (i > 2000000):
		break
	if isPrime(i):
		primes.append(i)
		t+= i
	i+=2

print "number of primes:", len(primes)
print "last prime:", primes[-1]
print "sum =", t
toc = time.time() - tic
print "time: ", toc