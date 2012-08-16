"""
Created by Kirk Anthony Boyer
7/10/2012
Solution to Project Euler Problem 27
	Problem:	Find the quadratic of the form q(n) = n^2 + an + b, with |a|, |b| < 1000, 
				that produces the most primes for consecutive values of n, starting with 0
	Idea:		-Clearly b must be prime, since q(0) = b must be prime.
				-b should be positive so that q(n) for small n is not negative
				-Brute force shouldn't take that long for this
"""
import math
import time
tic = time.time()

def largestPrimeFactor(n):
	i = int(math.sqrt(n))
	while not n%i==0:
		i-=1
	if i==1:
		return n
	return max(largestPrimeFactor(i),largestPrimeFactor(n/i))

def isPrime(n):
	if n == largestPrimeFactor(n):
		return True
	return False

#define a quadratic as a triplet of coefficients a, b, c, so an^2 + bn + c
#we are looking for triplets with a = 1, so we only need to store b and c
m = [1,41,39] # m is [b, c, number of primes produced]
primes = [43]

i = 47
while primes[-1] < 1000:
	if isPrime(i):
		primes.append(i)
	i+=4
	if (i > 1000):
		break
	if isPrime(i):
		primes.append(i)
	i+=2

for c in primes:
	for b in range(-(c-1),999):
		n = 1
		cont = True
		while (n*n + b*n + c > 0) and isPrime(n*n + b*n + c):
			n += 1
		n -= 1
		if n > m[2]:
			m = [b, c, n]

toc = time.time() -tic
print "n^2 +",m[0],"n +",m[1]," produces", m[2], "consecutive primes."
print m[0], "*", m[1], "=", m[0]*m[1]
print "took", toc, "seconds."