"""
Created by Kirk Anthony Boyer
7/9/2012
Solution to Project Euler problem 23
	Problem:	Find the sum of the positive integers which cannot be written as
				the sum of two positive abundant integers.
	Idea:		The problem suggests we need to check all numbers below 28123, so 
				we'll do that.
				
				We'll need some functions we made earlier (prime factorizations and
				the divisor function).
				
				I had a stupid error that made me get the wrong answer for SO LONG,
				that at the moment I don't care to both more to make this code
				run efficiently.
				
				I was (accidentally) including 0 in the list of abundant numbers,
				which threw off my answer by a factor of 995 (basically by making me
				count four abundant numbers as, themselves, able to be written as the
				sum of two other abundant numbers, when they are in fact not able). This
				was surprisingly hard to troubleshoot.
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

def isAbundant(n):
	k = divisorFunction(n) 
	if k > n:
		return True
	return False

#now we'll make a list of the abundant numbers below 20161 so we can quickly
#check if a given number is a sum of two of them


abundants = []
for i in range(1,28123):
	if isAbundant(i):
		abundants.append(i)


#now we'll make a set of all the numbers that are not the sum of two numbers in the
#set of abundant numbers

answer = set(range(1,28124))


"""
for a in abundants:
	for b in abundants:
		if (a+b) in answer:
			answer.remove(a+b)
"""
abundants.sort()
for i in range(len(abundants)):
	for j in range(i,len(abundants)):
		if (abundants[i] + abundants[j]) in answer:
			if (abundants[i] + abundants[j]) < 28124:
				answer.remove(abundants[i] + abundants[j])


print "sum of dems be:", sum(answer)
toc = time.time()-tic
print "took this longzzz:", toc, "seconds"