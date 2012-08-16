"""
Created by Kirk Anthony Boyer
7/10/2012
Solution to Project Euler Problem 29
	Problem:	How many distinct terms take the form a^b for 2 <= a,b <= 100?
	Idea:		Use python's built-in set class, Brute Force it all the way.
"""
import time
tic = time.time()
nums = set()
for a in range(2,101):
	for b in range(2,101):
		nums.add(pow(a,b))
toc = time.time()-tic
print "there are",len(nums),"distinct terms of the form a^b with 2 <= a,b <= 100."
print "took,", toc, "seconds."