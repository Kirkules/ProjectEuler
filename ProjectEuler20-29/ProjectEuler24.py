"""
Created by Kirk Anthony Boyer
7/9/2012
Solution to Project Euler Problem 24
	Problem:	What is the millionth lexicographic permutation of 0123456789?
	Idea:		No Code Necessary (tm)!
						
				In lexicographic order, the digit 0 is in the first place for all possible
				permutations of the remaining 9 digits, i.e. for 9! permutations. Then the
				digit 1 is in the first place for 9! permutations, etc. 
				
				Since 2*(9!) is less than 1 million and 3*(9!) is more than 1 million, we 
				go through all of the permutations with 0 and with 1 in front, but not all
				of the ones with 2 in front; thus, 2 is the first digit of the millionth
				lexicographic permutation.
				
				Now, once 2 is the first digit, there are 8! permutations for which 0 is
				the second digit, then 8! permutations for which 1 is the second digit,
				etc.
				
				In this way, we can see that the solution to the 9-variable equation:
				0 = 999,999 - a(9!) - b(8!) - c(7!) - d(6!) - e(5!) - f(4!) - g(3!) - h(2!) - i(1!)
				tells us, in fact, how to find the millionth lexicographic permutation.
				
				(The reason we use 999,999 instead of 1,000,000 is that this counts the
				 number of "moves" from the "first" permutation, rather than being a
				 strict index of the permutations. So the 1,000,000th lexicographic
				 permutation is 999,999 moves from the 1st, and *this* is the information
				 we can actually use to find the identity of this permutation)
				
				We start with 0123456789 and since a is 2, move the element at index 2
				(with indices starting at 0) to the left. So, now we have 2013456789. 
				
				Store the first digit and do the same thing with the remaining digits, 
				but this time with b instead of a. Since b is 6, we start with 013456789
				and move the 6th digit, which is 7, to the front, getting 701345689.
				
				Storing 7 (so that now the stored answer is 27), we move on to c, and 
				proceed in the obvious way.
				
				Since the solution to the equation above is:
				a=2
				b=6
				c=6
				d=2
				e=5
				f=1
				g=2
				h=1
				i=1
				This solution can be arrived at by trial and error fairly quickly, as
				hinted at in the above description of how to arrive, in the first place,
				at the equation. But it can also be solved using wolfram alpha or google
				calculator or mathematica or maple or matlab (etc.).
				
				Following the process described above, we get:
				0123456789		a = 2				answer = ?
			 -> 2 013456789							
			 => 013456789		b = 6				answer = 2
			 -> 7 01345689							
			 => 01345689		c = 6				answer = 27
			 -> 8 0134569
			 => 0134569			d = 2				answer = 278
			 -> 3 014569
			 => 014569			e = 5				answer = 2783
			 -> 9 01456
			 => 01456			f = 1				answer = 27839
			 -> 1 0456
			 => 0456			g = 2				answer = 278391
			 -> 5 046
			 => 046				h = 1				answer = 2783915
			 -> 4 06
			 => 06				i = 1				answer = 27839154
			 -> 6 0
			 => 0									answer = 278391546
			 And finally, tack on the last remaining digit, which is 0, here.
			 answer = 2783915460
"""