"""
Created by Kirk Anthony Boyer
7/8/2012
Solution to Project Euler Problem 11
	Problem: Find the greatest product of 4 adjacent numbers (in a line?!) in the
				provided grid:
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

	Idea: 	(at first) we are going to assume we are looking for products of
			sets of 4 adjacent numbers that are collinear (no squares or "L"s of
			numbers).
			
			So, there are four configurations in which such numbers can appear
			in the given grid: horizontal, vertical, and two diagonals. To find the
			particular set that has the highest product (and, more importantly, to
			*know* that it has the highest product) of any such set, we need to check
			the product of all possible quadruples. 
			
			To do this efficiently one might consider a similar solution to that used
			in the solution to PE#8, but this doesn't provide quite as much of an
			improvement because at the end of each line in the grid we will need to 
			reset (rather than just "replacing" the first and last numbers) anyway.
			
			In that light, the first attempt will be a simple brute-force search.
			
			At the very least, we won't have to duplicate each orientation for
			directionality, since real # multiplication is commutative.
"""
grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08n\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00n\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65n\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91n\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80n\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50n\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70n\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21n\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72n\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95n\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92n\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57n\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58n\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40n\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66n\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69n\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36n\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16n\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54n\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
grid = grid.split('n')
for i in range(len(grid)):
	grid[i] = grid[i].split(' ')
	
for i in range(len(grid)):
	for j in range(len(grid[i])):
		grid[i][j] = int(grid[i][j])
		
"""
Dirty work complete. grid is now a 2-dimensional array representing the correct #s
	[0][0] represents the top-left corner of the grid.
	COMMENCE THE COMPUTING!
"""
#initialize maximal product-tracker
max = 0
#also remember the matrix indices of the numbers that contributed
mi = [[0,0],[0,1],[0,2],[0,3]]

#__________horizontals_____________
for i in range(len(grid)):
	for j in range(len(grid[i])-3):
		test = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
		if test > max:
			max = test
			mi = [[i,j], [i,j+1], [i,j+2], [i,j+3]]


#___________verticals______________
for i in range(len(grid)-3):
	for j in range(len(grid[i])):
		test = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
		if test > max:
			max = test
			mi = [[i,j], [i+1,j], [i+2,j], [i+3,j]]

#_______neg-slope diagonals________
for i in range(len(grid)-3):
	for j in range(len(grid[i])-3):
		test = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
		if test > max:
			max = test
			mi = [[i,j], [i+1,j+1], [i+2,j+2], [i+3,j+3]]

#_______pos-slope diagonals________
for i in range(len(grid)-3):
	for j in range(len(grid[i])-3):
		test = grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j]
		if test > max:
			max = test
			mi = [[i,j+3], [i+1,j+2], [i+2,j+1], [i+3,j]]

print "max product of ", max," at indices ", mi
print "contributing numbers were: ", grid[mi[0][0]][mi[0][1]], grid[mi[1][0]][mi[1][1]]\
, grid[mi[2][0]][mi[2][1]], grid[mi[3][0]][mi[3][1]]