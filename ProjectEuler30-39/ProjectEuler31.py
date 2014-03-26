"""
Created by Kirk Anthony Boyer
7/10/2012
Solution to Project Euler Problem 31
	Problem:	How many ways can 2 pounds (english currency) be made up of any number
				of coins?
	Idea:		Brute force. Kind of a meh problem :/.
"""
import time
tic = time.time()
count = 1 #start with 1 for the 2-pound coin
for a in range(2+1):											# 1-pound coins
	for b in range(4+1-a):										# 50p coins
		for c in range(10+1-b):								# 20p coins
			for d in range(20+1-c):							# 10p coins
				for e in range(40+1-d):						# 5p coins
					for f in range(100+1-e):					# 2p coins
						for g in range(200+1-f):				# 1p coins
							if 100*a+50*b+20*c+10*d+5*e+2*f+g == 200:
								count += 1
toc = time.time() - tic
print "There are", count, "ways to make 2 pounds from coins."
print "Took", toc, "seconds."