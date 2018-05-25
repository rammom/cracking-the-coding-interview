#
#	Problem 3
#
'''
	Given a small string a and a larger string b, find all permutations of a in b.
	Print the location of each.
'''

#	Brute force, I'm going to itterate through each permutation of a and check
# 	for its location in b
#
# check if a is in b and return location, else return -1
def check_location(a, b):
	for i in range(len(b)-len(a)):
		if (a == b[i:i+len(a)]):
			print(a, " @ " ,i)
# find each permutation
def solution1(a, b):
	



