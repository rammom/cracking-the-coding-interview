#
#	Defined algorithms for easier use in code
#

'''
	COUNTING SORT
	@params: array of integers
	@return: sorted array

	O(n) time
	O(n) space

	!! NOTE: currently only works for integer values less than 1000 !!
		fix this
'''
def counting_sort(array):
	counter = [0]*1000
	for elem in array:
		counter[elem] += 1
	newArray = []
	for j in range(len(counter)):
		for i in range(counter[j]):
			newArray.append(j)
	
	return newArray
		
