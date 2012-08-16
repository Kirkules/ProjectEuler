"""
Created by Kirk Anthony Boyer
7/5/2012
Solution to Project Euler Problem 9
	Problem: 	Find the unique Pythagorean triple with a + b + c = 1000.
	Idea:		Use Stifel's and Ozanam's methods of generating triples;
				hope for luck!
				
				Neither Stifel's nor Ozanam's method directly yields the answer.
				
				However: Ozanam's method (on the first iteration) yields the triple:
					(8,15,17), for which 8+15+17=40.
				
				Since 1000 = 40*25, and multiplying each member of triple by any
					natural number yields another triple, we can get a triple whose
					sum is 1000 by multiplying (8,15,17) by 25, i.e. (200,375,425),
					the answer.
"""
import math
def gcd(a, b):
	if b > a:
		return gcd(b,a)
	if b == 0:
		return a
	return gcd(b, a-b)

def reduce(frac):
	g = gcd(frac[0], frac[1])
	return [frac[0]/g, frac[1]/g]




#Stifel's method
f = [1,1]
for i in range(1,50):
	j = 2*i+1
	f[0] = (i*j)+i
	f[1] = j
	f = reduce(f)
	c = math.sqrt( f[0]*f[0] + f[1]*f[1] )
	#if f[0]+f[1]+c == 1000:
	print "a + b + c =", f[0], "+", f[1], "+", c, "=", f[0]+f[1]+c
	

#Ozanam's method
f = [1,1]
for i in range(1,50):
	f[0] = 4*i*i + 8*i +3
	f[1] = 4*i + 4
	f = reduce(f)
	c = math.sqrt( f[0]*f[0] + f[1]*f[1] )
	#if f[0]+f[1]+c == 1000:
	print "a + b + c =", f[0], "+", f[1], "+", c, "=", f[0]+f[1]+c

	
	