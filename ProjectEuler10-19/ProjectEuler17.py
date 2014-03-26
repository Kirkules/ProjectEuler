"""
Created by Kirk Anthony Boyer
7/9/2012
Solution to Project Euler Problem 17
	Problem:	how many letters are used in writing the words for the #s 1 to 1000?
	Idea:		split into groups that are repeated in the linguistic constructions
"""

#counting number of letters in 1-9
num =  "one\
two\
three\
four\
five\
six\
seven\
eight\
nine"
a = len(num)
#result was 36

#counting number of letters in 10-19
num = "ten\
eleven\
twelve\
thirteen\
fourteen\
fifteen\
sixteen\
seventeen\
eighteen\
nineteen"
b = len(num)
#result was 70

#counting number of letters in 20, ..., 90
num = "twenty\
thirty\
forty\
fifty\
sixty\
seventy\
eighty\
ninety"
c = len(num)

#counting number of letters in 21-29, 31-39, ..., 91-99
d = 9*c + 8*a
#result was 702

#counting number of letters in 100, 200, ..., 900
e = a + 9*len("hundred")
#result was 99

#counting number of letters in 101, 102, ..., 998, 999
f = 99*e + 891*len("and") + 9*(a+b+c+d)
#result was 20160

total = a+b+c+d+e+f+len("onethousand")

print "1-9 together have", a, "letters."
print "10-20 together have", b, "letters."
print "20, 30, ..., 90 together have", c, "letters."
print "21-29, ..., 91-99 together have", d, "letters."
print "1-99, then, have", a+b+c+d, "letters."
print "100, 200, ..., 900 together have", e, "letters."
print "#01-#99 for # in {1, 2, ..., 9} together have", f, "letters."
print "So, all together, the numbers 1-1000 have", total, "letters."