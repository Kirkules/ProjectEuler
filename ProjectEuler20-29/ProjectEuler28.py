"""
Created by Kirk Anthony Boyer
7/10/2012
Solution to Project Euler Problem 28
	Problem:	In a 1001x1001 spiral, what is the sum of the numbers on the diagonals?
	Idea:		No Code Required (tm)!
				The gap between the indices on the diagonals clearly increases by 2 after
				each set of numbers on the diagonals.
				
				We can use the following 5x5 spiral as a visual example:
								21 22 23 24 25
								20  7  8  9 10
								19  6  1  2 11
								18  5  4  3 12
								17 16 15 14 13				
								
				A very simple view of the situation arises: The first group is:
				1+2 = 3, 	1+2(2) = 5, 	1+3(2) = 7, 	1+4(2) = 9.
					sum = 4(1) + 10(2) = 24
				The second group is
				9+4 = 13,	9+2(4) = 17,	9+3(4) = 7,		9+4(4) = 25.
					sum = 4(9) + 10(4) = 76
				The third group will be
				25+6 = 31,	25+2(6) = 37,	25+3(6) = 43,	25+4(6) = 49.
					sum = 4(25) + 10(6) = 160
					
				Following the pattern...
				The sum of the nth group of numbers on the diagonal, which has numbers
				separated by 2n, is 4(2n-1)^2 + 10(2n) = 4(4n^2 -4n +1) +20n, or
				16n^2 -16n +4 +20n, which is just 16n^2 +4n +4. The "0"th group, which is
				just 1, in the center, is a special case, so we won't use the formula for
				it.
				
				In an nxn spiral, we will go to the floor(n/2)th group of diagonal
				numbers. In the 5x5 example above, we'll go up to floor(2.5)=2 groups.
				
				So, the total sum that we will want is 1 plus the sum of the subsequent
				sum for each group, yielding the sum over i from 1 to floor(n/2) of
				16i^2 +4i +4, which we can reduce using known formulae.
				
				Ultimately, the expression for the sum of the numbers on the diagonal of
				an nxn spiral is (letting k = floor(n/2) ):
							16k(k+1)(2k+1)/6 + 4k(k+1)/2 + 4k + 1
				which simplifies to:
							(16/3)k^3 + 10k^2 + (26/3)k +1
							
				So, since we want the result for a 1001x1001 spiral, and floor(1001/2)
				is 500, we'll plug in 500 and we're good to go!
				
				The answer, then, is: 669171001
"""
import time
tic = time.time()
n = 1001
k = n/2
print (16*k*k*k + 30*k*k + 26*k)/3
print "took", time.time()-tic, "seconds!"