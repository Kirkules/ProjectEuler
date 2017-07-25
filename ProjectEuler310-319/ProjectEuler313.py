"""
Created by Kirk Anthony Boyer
7/13/2012
Solution to Project Euler problem 313
	Problem:	In a sliding game a counter may slide horizontally or vertically into an
				empty space. The objective of the game is to move the red counter from 
				the top left corner of a grid to the bottom right corner; the space 
				always starts in the bottom right corner.
				Let S(m,n) represent the minimum number of moves to complete the game on
				an m by n grid. For example, it can be verified that S(5,4) = 25.
				For how many grids is S(n,m) = p^2, where p < 1million is prime?
	Idea:		i		S(n,n) = 8n - 11
				ii		S(n,m) = S(m,n) by symmetry
				iii		S(n,m) = 6m + 2n -13 if m > n    (if n > m, replace using ii)
				
				S(n,m) is on the order of (but always less than) 8m, where m >= n.
				so only check for m < 1,000,000 / 8
				
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
	
#generate a list of the primes under a million
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

def S(a,b):		#assumes a, b are positive integers
	if a == b:
		return 8*a - 11
	elif a > b:
		return 6*a + 2*b - 13
	return 6*b + 2*a - 13

def isPrimeSquare(n):
	k = math.sqrt(n)
	if k == int(k):
		if isPrime(k):
			return True
	return False



count = 0
for p in primes:
	stdout.write('\r\x1b[K'+'Current prime: '+str(p))
	stdout.flush()
	if p == 2 or p == 3:		#skip 2 and 3 since their squares are so small, they
		count += 1				#mess up later calculations
		continue
	if (p*p + 11)%8 == 0: 		#if p^2 is of the form 8n - 11...
		count += 1				#count 1 board, since there can only be 1 solution n
								#to p^2 = 8n - 11
								
	#count two boards for each solution of p^2 = 6m +2n - 13
	k = (p*p + 13)/2
	count += (k/2)/3
	if (k/2)%3 != 2:
		count -= 1
	"""
	for n in range(2,(k/4)+1):
		if (k-n)%3 == 0:
			count += 2
	"""
	

		
print
print count, "such grids."
print "took", time.time()-tic, "seconds."