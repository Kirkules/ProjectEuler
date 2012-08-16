"""
NumberTheoryUtility.py
Created by Kirk Anthony Boyer
7/8/2012
This file will collect functions useful in many number-theoretic settings.
list of functions:
	gcd(a,b)
	largestPrimeFactor(n)
	primeFactorization(n)
	isPrime(n)
	divisorCount(f)
	divisorFunction(n)
	isPandigital(n)
	
"""

"""
TO PRINT ON THE SAME LINE, OVERWRITING OLD TEXT, DO:

stdout.write('\r\x1b[K'+STR)
stdout.flush()

WHERE STR IS A VARIABLE CONTAINING THE STRING YOU WANT TO PRINT
"""


import math

"""
gcd(a, b)
	returns the gcd of two integers. uses an iteratively implemented version of the 
	euclidean algorithm; this is the fastest algorithm+implementation of which I am
	aware for finding the gcd, and it also doesn't have pitfalls like recursion depth
	errors for weird numbers with large prime factors that are also relatively prime
	
example:
	input: 45, 30
	output: 15
"""
def gcd(a,b):
	if a < b:
		temp = b
		b = a
		a = temp
	while b > 0:
		temp = b
		b = a % b
		a = temp
	return a


"""
largestPrimeFactor(n)
requires:
	none
	
example:
	input: 99
	output: 11
"""
def largestPrimeFactor(n):
	i = int(math.sqrt(n))
	while not n%i==0:
		i-=1
	if i==1:
		return n
	return max(largestPrimeFactor(i),largestPrimeFactor(n/i))

	
"""
primeFactorization(n)
requires:
	largestPrimeFactor(n)

example:
	input: 28
	output: [ [2,2], [7,1] ]
"""
def primeFactorization(n):
	factors = [[1,1]]
	last = 1
	
	while n > 1:												#while there are still factors...
		p = largestPrimeFactor(n)
		lastIndex = len(factors)-1
		
		if factors[lastIndex][0] == p:    						# if the prime is repeated...
			factors[lastIndex][1] = factors[lastIndex][1] + 1 	# add to its multiplicity
		else:
			factors.append([p,1])								#otherwise add new factor item
		
		n = n/p
		
	factors.pop(0) #get rid of the "[1, 1]" placeholder factor
	factors.reverse()
	return factors
	
	
	
	
	
	
"""
isPrime(n)
requires:
	largestPrimeFactor(n)
	
example:
	input: 408
	output: False
"""
def isPrime(n):
	if n == largestPrimeFactor(n):
		return True
	return False







"""
divisorCount(f)
	Uses the idea of the Divisor function to find how many divisors divide the number whose
	factorization is given by f
parameters:
	f: the result of a primeFactorization(n) call; an mx2 array of primes & their powers

example:
	input:[ [2,2], [7,1] ]            ( = primeFactorization(28) )
	output: 6
"""
def divisorCount(f):
	count = 1
	for factor in f:
		count = count * (1 + factor[1])
	return count

"""
divisorFunction(n)
	sums the divisors of n

example:
	input: 6
	output: 6
	
	input: 24
	output: 60
"""
def divisorFunction(n):
	#s(N) = prod_{i=1}^{r} [(p_i)^(a_i + 1) - 1] / [p_i - 1]
	#d(N) = s(N)-N
	prod = 1
	for prime in primeFactorization(n):
		prod *= (math.pow(prime[0], prime[1] + 1) - 1) / (prime[0] - 1)
	d = prod - n
	return int(d)

"""
isPandigital(s)
	returns whether or not s is pandigital (whether the characters in s are repeated)
	
example:
	input: '41234'
	output: False
	
	input: '984135276'
	output: True
	
	input: 'samuel in cryo'
	output: False (spaces are duplicated)
"""
def isPandigital(s):
	history = ''
	for digit in s:
		if digit in history:
			return False
		if digit == '0':#arbitrary definition of pandigital does not include digit 0
			return False
		history += digit
	return True



"""
fastPowering(a,b,c)
	returns a^b (mod c), using the fast powering algorithm
	
example:
	input: (3,218,1000)
	output: 489
			(equivalent to 3^218 mod 1000)
I left the un-streamlined version here for reference; use the version simply called
 "fastPowering(a,b,c)"
def unstreamlinedFastPowering(a,b,c):
	#first find the binary representation of the power, b
	binary_b = bin(b)
	#remove the "0b" at the beginning
	binary_b = binary_b[2:]
	#reverse the string so that index i represents the 2^i part in the binary rep.
	binary_b = binary_b[::-1]
	
	#for each "1" in binary_b, calculate the power of a corresponding to the power of
	#2 that is represented by that 1's position in the binary representation
	
	product = 1
	a_power = a #start with a^1, i.e. the first power of a is a^( 2^0 = 1 )
	for i in range(len(binary_b)):
		if binary_b[i] == '1':
			product *= a_power 	#multiply by the current 2-power exponent of a
			product %= c		#mod by c at each step for even smaller multiplications
		a_power = a_power**2
	return product
"""

def fastPowering(a,b,c):
	product = 1
	a_power = a
	while b > 0:
		bit = b%2
		if bit == 1:
			product *= a_power
			product %= c
		a_power = a_power**2
		b /= 2
	return product


