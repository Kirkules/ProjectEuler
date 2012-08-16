"""
Created by Kirk Anthony Boyer
7/19/2012
Solution to Project Euler Problem 38
	Problem: 	Take the number 192 and multiply it by each of 1, 2, and 3:
				192  1 = 192
				192  2 = 384
				192  3 = 576
				By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 
				192384576 the concatenated product of 192 and (1,2,3)
				
				The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving 
				the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
				
				What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
				concatenated product of an integer with (1,2, ... , n) where n  1?
				
	Idea: 		We need only explore pandigitals larger than 918273645, since that is one
				which can be formed as described. (This is still quite a few numbers)
				
				The first thing to do to solve this problem is to find an algorithm that
				determines whether a given 9-digit number (pandigital or not) is the 
				concatenated product of some integer with (1,...,n).
				
				Since we don't know how many digits the numbers will each split up into,
				we'll start with the first digit, and see if the following digit(s) are 
				two times that number. If so, check if the next digits are three times
				the first digit, and so on. If the last check succeeded and we have no
				digits left in the pandigital candidate to check, then we have found a
				number that fits our criteria.
				
				If that test doesn't work (starting with the first digit), we start with
				the first two digits and proceed in the same fashion. This test needs to
				be performed (unless it succeeds at some point) on the first 1 digit, the
				first 2, the first 3, the first 4, and the first 5 digits. 
				
				(a 9-digit number cannot be the concatenated product of a k>5
				digit number with (1,...,n) for any n)
				
				
"""
import time
def isConcatenatedProduct(n):#seems to take about 40ms per call.

	#if so...
	for i in [1,2,3,4,5]:
		name = str(n)
		first = name[0:i]
		name = name[i:]
		t = 2
		while name != '':
			if name.startswith(str(t*int(first))):
				t += 1
				name = name[len(str(t*int(first))):]
				continue
			else:
				break
		#if we broke the loop without getting rid of all the characters
		if name != '':
			#and we've gone through all the first-k-digits tests
			if i == 5:
				#then return false
				return False			
		#otherwise, if we broke the loop and got rid of everything, quit testing
		else:
			break
	#if we got out of the loop and everything worked, we've found a conc.product. number
	return True

#now, for brute force, iterate through the pandigitals greater than 918273645
#and keep track of the biggest
top = 918273645
#	  abcdefghi
duplicates = set()

tic = time.time()
for a in range(9,9+1):
	duplicates = set()
	duplicates.add(a)
	for b in range(1,9+1):
		if b in duplicates:
			continue
		duplicates.add(b)
		for c in range(1,9+1):
			if c in duplicates:
				continue
			duplicates.add(c)
			for d in range(1,9+1):
				if d in duplicates:
					continue
				duplicates.add(d)
				for e in range(1,9+1):
					if e in duplicates:
						continue
					duplicates.add(e)
					for f in range(1,9+1):
						if f in duplicates:
							continue
						duplicates.add(f)
						for g in range(1,9+1):
							if g in duplicates:
								continue
							duplicates.add(g)
							for h in range(1,9+1):
								if h in duplicates:
									continue
								duplicates.add(h)
								for i in range(1,9+1):
									if i in duplicates:
										continue
									n = a*10**8 + b*10**7 + c*10**6 + d*10**5 + e*10**4 + f*10**3 + g*10**2 + h*10 + i
									if isConcatenatedProduct(n):
										print n, "is a concatenated product."
								duplicates.remove(h)
							duplicates.remove(g)
						duplicates.remove(f)
					duplicates.remove(e)
				duplicates.remove(d)
			duplicates.remove(c)
		duplicates.remove(b)
	duplicates.remove(a)

toc = time.time()-tic

print "Took", toc, "seconds."