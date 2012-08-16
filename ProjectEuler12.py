"""
Created by Kirk Anthony Boyer
7/8/2012
Solution to Project Euler Problem 12
	Problem:Find the first triangular number with more than 500 factors.
	
	Idea: 	Given the prime factorization of a number, k = (p^a)(q^b)...*(r^c),
			the number of divisors of k is (1+a)(1+b)...(1+c).
			
			Since the closed form of the nth triangular number is n(n+1)/2
			and exponents in products are additive, we can calculate the
			prime factorization of n and n+1, and perform a quick calculation
			afterward to find the number of factors of the nth triangular
			number.
			
			So we'll need functions for: 
				-calculate divisors of n
				-calculate prime factorization of n
					(iterated use of project euler problem 3)
			
			The reason we keep track of the factors and not just their
			multiplicities (which are all are needed for the divisor function)
			is so that we can calculate the factorizations of smaller numbers and
			combine them.
"""
import math

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
			factors.append([p,1])							#otherwise add new factor item
		
		n = n/p
		
	factors.pop(0) #get rid of the "[1, 1]" placeholder factor
	factors.reverse()
	return factors

"""
divisorCount(f)
	Uses the Divisor function to find how many divisors divide the number whose
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
combineFactorizations(f1, f2)
	Takes the prime factorizations of two numbers and returns the prime factorization
	of their product. This method takes advantage of the fact that the factorizations
	given by primeFactorization(n) are ordered from smallest to largest prime factor.

parameters:
	f1, f2: the result of a primeFactorization(n) call
	
example:
	input: [ [2,2], [7,1] ]       ,         [ [2,4], [17,2] ]
	output: [ [2,6], [7,1], [17,2] ]
"""
def combineFactorizations(F1, F2):
	f1 = list(F1)
	f2 = list(F2)
	k = len(f1)+len(f2)
	result = []
	for i in range(k):
		if (not (f1==[])) and (not (f2==[])):
			if f1[0][0] < f2[0][0]:			#if next prime in f1 is smaller
				result.append(f1.pop(0))
			elif f1[0][0] > f2[0][0]:
				result.append(f2.pop(0))	#if next prime in f2 is smaller
			else:							#if next prime is same in f1 and f2
				temp1 = f1.pop(0)
				temp2 = f2.pop(0)
				result.append([ temp1[0], (temp1[1] + temp2[1]) ])
				
		elif (f1==[]) and (not (f2==[])):
			result.append(f2.pop(0))
		elif (not (f1==[])) and (f2==[]):
			result.append(f1.pop(0))
		else:
			break

	return list(result)




def factToNumber(f):
	n = 1
	for factor in f:
		n *= math.pow(factor[0],factor[1])
	return n
	
	
	

#############################################################
#begin problem 12 solution
#############################################################

n = 6
f_n = primeFactorization(n)
f_n1 = primeFactorization(n+1)

done = False
while not done:
	n += 1
	f_n = f_n1[:]
	f_n1 = primeFactorization(n+1)
	#f_n = primeFactorization(n)
	#f_n1 = primeFactorization(n+1)
	f = combineFactorizations(f_n, f_n1)
	f[0][1] -= 1		#take out a factor of 2 so f is factorization of n(n+1)/2
	c = divisorCount(f)
	#print "T_", n, "=", factToNumber(f), "=", f,  " has ", c, " divisors."
	if c>500:
		done = True
		print "T_", n, "=", factToNumber(f), "=", f,  " has ", c, " divisors."
