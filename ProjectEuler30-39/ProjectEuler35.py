"""
Created by Kirk Anthony Boyer
7/12/2012
Solution to Project Euler Problem 35
	Problem: 	Find the number of circular primes below 1,000,000
	Idea: 		Find the primes below 1,000,000 and check if their digit-rotations are
				also in the list
			
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

def nextRotation(n):
	if n < 10:
		return n
	digit = n%10
	n /= 10
	n = digit * (10**len(str(n))) + n
	return n


circprimes = []


for p in primes:
	s = str(p)
	#if one of the digits of p is even, one of the rotations will be a multiple of 2
	if ('0' in s) or ('2' in s) or ('4' in s) or ('6' in s) or ('8' in s):
		continue
	
	#if we already found p as the rotation of another prime
	if p in circprimes: 
		continue
	
	stdout.write('\r\x1b[K'+'Checking ' + str(p))
	stdout.flush()
	cont = False
	
	#check rotations of p, see if they are prime
	r = nextRotation(p)
	while r != p:
		
		#if even one is not, go to next prime p
		if r not in primes:
			cont = True
			break
		r = nextRotation(r)

	if cont:
		continue

		#if all rotations were also prime, add them all to the list of circular primes
	else:
		circprimes.append(p)
		r = nextRotation(p)
		while r != p:
			circprimes.append(r)
			circprimes.sort()
			r = nextRotation(r)

circprimes = list(circprimes)
circprimes.sort()
print "circular primes < 1million:", circprimes
print "there are ", len(circprimes), "circular primes below 1million"
toc = time.time() - tic
print "time: ", toc