#	2018.05.20
#	Mostapha Rammo
#	Cracking the Coding Interview
'''
	Problem:
		Given an array of distinct integer values, count the number of pairs of integers that have the
		difference k.
	Example:
		Given an array {1, 7, 5, 9, 2, 12, 3} and difference k = 2, there are four pairs with difference 2.
'''

#
#	HELPER FUNCTIONS
#

''' Binary search '''
def find(array, val):
	index = len(array)//2
	if (index == 0):
		return array[index] == val;
	if (array[index] == val):
		return True
	elif (array[index] < val):
		return find(array[index:], val)
	elif (array[index] > val):
		return find(array[:index], val)
	
''' Merge sort '''
def merge(A, B):
	array = []
	a = 0
	b = 0
	for i in range(len(A) + len(B)):
		if (a > len(A)-1):
			array += B[b:]
			return array
		elif (b > len(B)-1):
			array += A[a:]
			return array
		if (A[a] <= B[b]):
			array.append(A[a])
			a+= 1
		else:
			array.append(B[b])
			b+=1
	return array

def mergeSort2(A, B):

	# base case
	if (len(A) == 1 and len(B) == 1):
		return merge(A, B)
	elif (len(A) == 1):
		return merge(A, merge(B[:len(B)//2], B[len(B)//2:]))
	elif (len(B) == 1):
		return merge(B, merge(A[:len(A)//2], B[len(A)//2:]))
	

	# recursive step
	return merge( mergeSort2(A[:len(A)//2], A[len(A)//2:]), mergeSort2(B[:len(B)//2], B[len(B)//2:]))

def mergeSort(array):
	return 	mergeSort2(array[:len(array)//2], array[len(array)//2:])
	
#
#	MAIN FUNCTIONS
#

# n^2 solution
def countDiff(array, k):
	counter = 0
	for i in range(len(array) - 1):
		for j in range (i+1, len(array)):
			if (abs(array[i] - array[j]) == abs(k)):
				counter += 1
	return counter

# nlogn solution
def countDiff2(array, k):
	counter = 0;
	# sort the array
	array = mergeSort(array)
	# itterate through the array,
	for i in range(len(array)):
		# do binary search to find "other side"
		if (find(array, array[i] + k)):
			counter += 1
		if (find(array, array[i] - k)):
			counter += 1
	return counter//2;

# n solution
def countDiff3(array, k):
	counter = 0;
	# throw elements into a hashtable
	elems = {}
	for i in array:
		elems[i] = True;
	for i in array:
		if ( i + k in elems ):
			counter += 1
		if ( i - k in elems ):
			counter += 1
	return counter//2;

array = [1, 7, 5, 9, 2, 12, 3]
k = 2
print(countDiff3(array, 2))
