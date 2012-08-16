"""
Created by Kirk Anthony Boyer
7/5/2012
Solution to Project Euler Problem 4
	Problem:	A palindromic number reads the same both ways. The largest palindrome
				made from the product of two 2-digit numbers is 9009 = 91 99.
				Find the largest palindrome made from the product of two 3-digit 
				numbers.
	Idea:	Brute force, starting from 999x999. I'll go through all 899 numbers for the
			pair to the left, larger number. Once I find one palindrome Ill iterate down
			only to the largest right-hand-side number that was in a palindrome so far,
			since the product involving lower right-hand-side numbers thereafter will be
			smaller than the palindrome I found. Once the left-hand-side iteration 
			reaches the largest right-hand-side number, the loop will end.
			
			
"""
def isPal(s):
	s = list(s)
	n = len(s)
	k = int(n/2)
	for i in range(k):
		if not s[i]==s[n-i-1]:
			return False
	print s
	return True

left = 0
right = 0
min = 100

for i in reversed(range(100,999)):
	for j in reversed(range(min,999)):
		if isPal(str(i*j)):
			print "new min = ", j
			min = j
			print i*j, left*right
			if ((i*j) > (left*right)):
				right = j
				left = i
			break
	if i==min:
		break
		
print "Best:", left, "x", right, " = ", left*right