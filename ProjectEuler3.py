"""
Created by Kirk Anthony Boyer
7/5/2012
Quick Solution to Project Euler Problem 3
	Problem: Given a natural number n, find its largest prime factor.
	
	Idea: 	Starting with the largest factor of n, we'll recursively
			look for the larget prime factor of each factor we've found.
			
			If we have a prime factor already, then we're done.
	
			The largest factors of n are closest to its square root 
			(among factors of n), so we'll start looking around sqrt(n)
			for factors of n, and let recursion do the dirty work.
			
			For simplicity/understanding, this is among the best solutions.
			It is not particularly efficient.
"""
import math
def LargestPrimeFactor(k):
	i = int(math.sqrt(k))

	while not k%i==0:
		i-=1
	if i==1:
		return k
	return max(LargestPrimeFactor(i),LargestPrimeFactor(k/i))
	
		
n = int(raw_input("Which number's largest prime factor to find?"))
x = LargestPrimeFactor(n)
print "The largest prime factor of ", n, " is: ", x
	