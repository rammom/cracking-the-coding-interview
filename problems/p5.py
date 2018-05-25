#
#	Problem 5
#
'''
	Given two sorted arrays, find matching elements
'''

# return true if elem found in array
def binary_search(array, elem):
	if (len(array) == 0):
		return False
	mid = len(array)//2
	if (elem == array[mid]):
		return True
	elif (elem < array[mid]):
		return binary_search(array[:mid], elem)
	else:
		return binary_search(array[mid+1:], elem)

# O(nlgn)
def solution1(A, B):
	for i in range(len(A)):
		if (binary_search(B, A[i])):
			print(A[i])


# O(n) time
# O(n) space
def solution2(A, B):
	map = {}
	for elem in a:
		map[elem] = True
	for elem in b:
		if (elem in map):
			print(elem)

# O(n) time
# O(1) space
def solution3(A, B):
	bIndex = 0
	for i in range(len(A)):
		for j in range(bIndex, len(B)):
			if (A[i] == B[j]):
				print(A[i])
			elif (A[i] < B[j]):
				break
			bIndex = j
			

a = [1,2,3,4,5]
b = [2,4,5,6,8]
solution3(a, b)	
