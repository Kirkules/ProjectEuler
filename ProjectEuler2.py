"""
Created by Kirk Anthony Boyer
7/5/2012
Quick Solution to Project Euler Problem 2
	Idea: 	Every term with index that is a multiple of 3 is even. This is because
			the sum of like-parity numbers is even, and the sum of unlike-parity
			numbers is odd; the sequence of of number parity pairings in the
			Fibonacci sequence is (odd + odd), (odd + even), (even + odd),
			and this pattern repeats cyclically.
"""


def Fib(z):
	z[0] = z[1]
	z[1] = z[2]
	z[2] = z[0] + z[1]
	return z
	
x = [1,1,2]
sum = 0

while x[2] < 4000000:
	sum += x[2]
	x = Fib(Fib(Fib(x)))

print sum