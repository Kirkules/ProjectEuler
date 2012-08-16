"""
Created by Kirk Anthony Boyer
7/5/2012
Solution to Project Euler Problem 7
	Problem: Find the 10,001st prime number.
	Idea: Sieve of Eratosthenes + brute force.
			-slight optimization: only check numbers equiv. to 1 or 5 (mod 6)
				*(reduced run time to ~6 seconds)
			-slight optimization: only check primes up to sqrt(i)
				*(reduced run time to ~0.17 seconds)
"""
import time
import math
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
	
i = 7 #equivalent to 1 (mod 6)
while len(primes) < 10001:
	if isPrime(i):
		primes.append(i)
	i+=4					#switch to a number = 5 (mod 6)
	if isPrime(i):
		primes.append(i)
	i+=2					#switch to a number = 1 (mod 6)
	
print primes[-1]
toc = time.time() - tic
print "time: ", toc