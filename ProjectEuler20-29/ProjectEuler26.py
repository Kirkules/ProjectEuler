"""
Created by Kirk Anthony Boyer
7/10/2012
Solution to Project Euler Problem 26
	Problem:	Which unit fraction (1/n) has the longest recurring cycle in its decimal
				representation, for n < 1000?
	Idea:		To use code for this problem, we need a way of detecting that a decimal
				representation does, indeed, have an (infinitely) recurring cycle, rather
				than just a segment that has a finitely recurring cycle.
				
				One idea is to simulate long division, and whenever a given step is
				identical (in terms of the number on the line and the rest of the
				quotient) to a step that has been executed previously, count how many steps
				were between those identical steps.
				
				The reason this yields the length of the repeating sequence is that 
				the divisor is always the same, and if the quotient at any step is the
				same as a previous step, what follows will also be the same, as we are
				still using the same rules for long division.
				
				So we need to keep track of a growing list of steps, and make sure we're
				performing the steps correctly, and we should be able to find the answer
				by brute force fairly quickly.
				
				For each divisor, terminate the search either: when a step is repeated,
				or when a step is 0 (no remainder after that step -> not a repeating
				decimal).
				
				One critical fact is that all rational decimals are terminal or repeating.
				
				example: 1/7
				   0.1 4 2 8 5 7 1
				  _______________________
				7 )1.0 0 0 0 0 0 0 0 0 0     <--|
				     7							|
				   ---							|
				     3 0						|
				     2 8						|
				     ---						|
				       2 0						|
				       1 4						|
				       ---						|  After 6 steps we are back to where
				         6 0					|  we started.
				         5 6					|
				         ---					|
				           4 0					|
				           3 5					|
				           ---					|
				             5 0				|
				             4 9				|
				             ---				|
				               1 0			 <__|
"""

"""
nextLongDivisionStep(d,r)
	Takes as a d = divisor, r= remainder, where, for example, if
	we are dividing 7 into 1 (i.e. 1/7), the divisor is 7 and the (first) remainder
	is 1. After the first step, the remainder is 3, and after the second step, the
	remainder is 2 (see above).
	
example:
	input:	[7,1]
	output:	[7,2]
	
	input:	[7,6]
	output: [7,4]
"""
import time
tic = time.time()

def nextLongDivisionStep(d,r):
	#find smallest power of 10 times remainder which is larger than divisor
	#    (may be 10^0 = 1)
	p = 0
	while r*pow(10,p) < d:
		p += 1
	r = r*pow(10,p)
	
	#find highest multiple of divisor less than above result
	m = 1;
	while m*d <= r:
		m+= 1
	m -= 1 #we will have overshot by 1, so take off 1
	
	#find difference between remainder times power of 10 and divisor's multiple
	diff = r - (m*d)
	#return [d, difference], as difference above is the new remainder
	return int(diff)


#time to check all divisors for repetition length
max = [1,1] #[divisor, length]
TOP = 1
for d in range(1,1000):
	record = []
	r = nextLongDivisionStep(d,TOP)
		#until we repeat or find remainder 0, do long division
	while (r not in record) and (r != 0):
		record.append(r)
		r = nextLongDivisionStep(d,r)
		#if we found a new longest cycle..
	if not (record == []):
		while (not (record == [])) and (record[0] is not r):
			record.pop(0)
	if ( (len(record) - 1) > max[1]) and (r != 0):
		max[0] = d
		max[1] = len(record) - 1
		
toc = time.time() - tic
print "max cycle length was", max[1], ", in", TOP, "/", max[0]
print "...took", toc, "seconds."