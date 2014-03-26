"""
Created by Kirk Anthony Boyer
7/12/2012
Solution to Project Euler problem 33
	Problem:	There are four non-trivial examples of fractions with 2-digit numerator
				and denominator whose simplified forms are 1-digit numerator/denominator
				fractions where the digits in the simplified n/d are represented in the
				2-digit n/d. Find the denominator of their product when simplified. 
	Idea:		Search space: 1-99 numerators, each paired with 1-99 denominators.
"""
import time
import string
tic = time.time()

def gcd(a, b):
	if b > a:
		return gcd(b,a)
	if b == 0:
		return a
	return gcd(b, a-b)

_a = '00'
_b = '11'
def shareDigits(a,b):
	_a = str(a)
	_b = str(b)
	for digit in _a:
		if digit in _b:
			return digit
	return False

def reduceFraction(num,den):
	g = gcd(num,den)
	while g > 1:
		num /= g
		den /= g
		g = gcd(num,den)
	return [num,den]

def fracsEquivalent(f1, f2):
	return (f1[0]*f2[1] == f1[1]*f2[0])
		

fracs = []

for d in range(10,99+1):
	for n in range(10,d):
		digit = shareDigits(n,d)
		#if there was a digit common to the numerator and denominator:
		if digit != '' and digit != False:
			k = reduceFraction(n,d)
			f = [int(string.replace(str(n), digit, '', 1)), int(string.replace(str(d),digit,'',1)) ]
			#if the reduced fraction is equivalent to "canceling" the shared digit:
			if fracsEquivalent(k,f):
				#and if the digit does not in fact divide the numerator and denominator
				if digit != '0':
					if n%int(digit) != 0 or d%int(digit) != 0:
						fracs.append([n,d])
#print "Fractions for which this works...", fracs
print "Took", time.time()-tic, "seconds."
print "Found", len(fracs), "fractions that work. They are:"
result = [1,1]
for frac in fracs:
	print frac[0], "/", frac[1], ", ", 
	result[0] *= frac[0]
	result[1] *= frac[1]
	
result = reduceFraction(result[0], result[1])
print "The denominator of the reduced form of their product is:", result[1]