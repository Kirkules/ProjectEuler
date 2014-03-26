"""
Created by Kirk Anthony Boyer
7/8/2012
Solution to Project Euler Problem 14
	Problem: The following rules define a sequence given positive integers n:
				n --> n/2 		(if n is even)
				n --> 3n + 1 	(if n is odd)
			 The sequence begins with any given positive integer.
			 It terminates when the result of a rule is 1.
			 
			 Find the number n < 1,000,000 which produces the longest sequence

	Idea:	First try: brute force, see how long it takes.
			(not long at all, it seems)
"""
def CollatzLength(n):
	length = 1
	while not (n==1):
		length += 1
		if (n%2 == 0):
			n = n/2
		else:
			n = 3*n + 1
	return length

max = 1
num = 2
for i in range(1000000):
	k = CollatzLength(i+1)
	if k > max:
		max = k
		num = i+1
		print max, " for n = ", i+1
		
print "max length is ", max, " for n = ", num