"""
Created by Kirk Anthony Boyer
7/9/2012
Solution to Project Euler Problem 18
	Problem: 	Find the monotone path from top to bottom of the following triangle
				with maximal sum of the numbers passed.
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

	Idea:	I'm not sure if this is a named-algorithm already, but I think of it as a sort
			of reverse-Dijkstra's algorithm.
			
			First, create a directed graph from the triangle. (direction is UPward, toward
			the single top-node of the triangle!)
			
			Make each node have the number corresponding to its place in the triangle,
			a "sum" value which represents the sum of values from the "highest-sum" 
			path below it.
			
			In a sense, we are solving smaller versions of the problem,
			for many, overlapping, smaller triangles, and combining solutions at each step.
			
			So, each step has a "current tier" of the triangle.
			
			At the second step, we are one tier up from the bottom, and we just look
			below to the left and right and see which node has the higher value sum, 
			add that sum to the current node's value. 
			
			At the third step, we are two tiers from the bottom and all the one-tier-up
			nodes have totals already. Repeat until we are at the very top tier.
			
			Once this process terminates, the top node's "sum" value will be the value of
			the highest-valued path.
			
			Optimizations include:
				-note that you only need the information/solutions for the previous tier
				 of the triangle, since information from all tiers before the previous
				 one has already been included. So don't keep track of all of it.
"""
num = "75n\
95 64n\
17 47 82n\
18 35 87 10n\
20 04 82 47 65n\
19 01 23 75 03 34n\
88 02 77 73 07 63 67n\
99 65 04 28 06 16 70 92n\
41 41 26 56 83 40 80 70 33n\
41 48 72 33 47 32 37 16 94 29n\
53 71 44 65 25 43 91 52 97 51 14n\
70 11 33 28 77 73 17 78 39 68 17 57n\
91 71 52 38 17 14 91 43 58 50 27 29 48n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

#convert the string to an array of arrays of integers
num = num.split('n')
for i in range(len(num)):
	num[i] = num[i].split(' ')

for i in range(len(num)):
	for j in range(len(num[i])):
		num[i][j] = int(num[i][j])


k = len(num) #number of tiers of the triangle

#initialize sums at 0 for an imaginary tier "below" the bottom tier
sums = []
for i in range(len(num[-1])+1):
	sums.append(0)

for i in range(k):						#for each tier (use k-i-1, for indexing from the back)
	newsums = []
	for j in range(len(num[k-i-1])):	#for each element in this tier...
		newsums.append(num[k-i-1][j] + max(sums[j], sums[j+1]))			#record best sum
	sums = list(newsums)				#remember the new results only

print "The top-tier element should now have one value, which is", sums[0]