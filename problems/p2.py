#
#	Problem 2
#
'''
	Find all solutions to a^3 + b^3 = c^3 + d^3
'''

#	Brute force O(n^4) solution
#
def solution1():

	for a in range(1, 1000):
		for b in range(1, 1000):
			for c in range(1, 1000):
				for d in range(1, 1000):
					if (a*a*a + b*b*b == c*c*c + d*d*d):
						print(a, b, c, d)


#	We can improve a little bit by computing the 
#	'd' value for each a, b, c instead of guessing
#	O(n^3)
#
def solution2():
	for a in range(1, 1000):
		for b in range(1, 1000):
			for c in range(1, 1000):
				d = Math.pow(a*a*a + b*b*b - c*c*c, 1/3)
				if (a*a*a + b*b*b == c*c*c + d*d*d):
					print(a, b, c, d)



#	Let's use a little bit of dynamic programming. 
#	Instead of recomputing all (c, d) pairs for every (a, b) pair,
#	lets keep a list of (c, d) pairs and find the matches from within 
#	the list.
#
def solution3():
	n = 1000
	map = {}
	for c in range(1, n):
		for d in range(1, n):
			result = c*c*c + d*d*d
			if (not result in map):
				map[result] = []
			map[result].append((c, d))
	
	for a in range(1, n):
		for b in range(1, n):
			result = a*a*a + b*b*b
			if (result in map):
				for pair in map[result]:
					print((a, b), pair);

			
#	We actually don't even need to itterate through all (a, b) pairs anymore
#	since all matched will already be in the map..
#
def solution4():
	n = 1000
	map = {}
	for c in range(1, n):
		for d in range(1, n):
			result = c*c*c + d*d*d
			if (not result in map):
				map[result] = []
			map[result].append((c,d))
			
	for l in map:
		for pair1 in map[l]:
			for pair2 in map[l]:
				print(pair1, pair2)

solution4()
