"""
Created by Kirk Anthony Boyer
7/9/2012
Solution to Project Euler problem 21
	Problem:	Find all the amicable numbers under 10000 (and sum them up).
	Idea:		From wolfram mathworld (originally Berndt 1985), for a given natural
				number N = ((p_1)^(a_1))*...*((p_r)^(a_r))    (prime factorization)
				
				The divisor function, whose value is the sum of the divisors of
				N, including N itself and 1, is:
				
				s(N) = prod_{i=1}^{r} [(p_i)^(a_i + 1) - 1] / [p_i - 1]
				
				So, stick this into a function, recall the prime factorization
				functions from earlier problems, and iterate over the numbers under 10000.
				
				Takes half a second, so I'm not going to try to optimize.
"""
import math
import time

tic = time.time()
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


def divisorFunction(n):
	#s(N) = prod_{i=1}^{r} [(p_i)^(a_i + 1) - 1] / [p_i - 1]
	#d(N) = s(N)-N
	prod = 1
	for prime in primeFactorization(n):
		prod *= (math.pow(prime[0], prime[1] + 1) - 1) / (prime[0] - 1)
	d = prod - n
	return int(d)

amicables = set()

for c in range(9999):
		if c < 2:
			continue
		k = divisorFunction(c)
		if (c == divisorFunction(k)): #if c and k are amicable
			if not (c==k):
				amicables.add(c)
				amicables.add(k)
			
amicables = list(amicables)
amicables.sort()
#candidates now should only contain amicable numbers 
toc = time.time() - tic
print amicables
print "sum: ", sum(amicables)
print "time: ", toc
			
				