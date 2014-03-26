"""
Created by Kirk Anthony Boyer
7/13/2012
Solution to Project Euler problem 34
	Problem:	Find all numbers which are equal to the sum of the factorials of
				their digits.
	Idea:		
"""
import time
def factorial(n):
	prod = 1
	for i in range(1,n+1):
		prod *= i
	return prod

def intList(n):
	l = []
	while n != 0:
		l.append(n%10)
		n /= 10
	l.reverse()
	return l


facts = [1]
for i in range(1,9+1):
	facts.append(factorial(i))

	
def sumFacts(digitList):
	s = 0
	for digit in digitList:
		s += facts[digit]
	return s

tic = time.time()

#we now have an array facts for which facts[n] = n! for 1 <= n <= 9
total = 0
for n in range(10,50000):
	if n == sumFacts(intList(n)):
		print n
		total += n

print "total is", total
print "took ", time.time()-tic, "seconds."
