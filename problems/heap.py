#
#	Heap as ADT (Priority Queue)
#

from helpers import swap

'''
	IS LEAF

	@params: heap, index
	@return: true if heap[index] is a leaf, false otherwise

	O(1) time and space
'''
def __is_leaf(array, index):
	if (__get_left_child(array, index) == False):
		return True
	return False

'''
	GET LEFT/RIGHT CHILD

	@params: heap, index
	@return: index of left/right child of index if exists, false otherwise
	
	O(1) time
	O(1) space
'''
def __get_left_child(array, index):
	location = index*2 + 1
	if (location > len(array)-1):
		return False
	return location

def __get_right_child(array, index):
	location = index*2 + 2
	if (location > len(array)-2):
		return False
	return location

'''
	MAX HEAPIFY
	
	@params: array to perform operation on, index location where to perform operation
	@return: None
	@info: Single operation on heap to build a max heap on the subtree at index
		this assumes array[index]'s left and right subtrees are heaps

	O(lgn) time
	O(1) space
'''
def __max_heapify(array, index):
	if (__is_leaf(array, index)):
		return array;

	rightIndex = __get_right_child(array, index)
	leftIndex = __get_left_child(array, index)

	if (array[index] > array[leftIndex]):
		if (not rightIndex == False and array[index] > array[rightIndex]):
			return;

	if (not rightIndex == False):
		if (array[rightIndex] > array[leftIndex]):
			array = swap(array, index, rightIndex)
			array = __max_heapify(array, rightIndex)
	else:
		array = swap(array, index, leftIndex)
		array = __max_heapify(array, leftIndex)
	return array
	
'''
	BUILD MAX HEAP	

	@params: array of integers
	@return: max heap
	@info: given an array of integers, we return a max heap with those values

	O(lgn) time
	O(n) space

	!! FAILS !!	
'''	
def build_max_heap(array):
	for i in range(len(array)//2-1, -1, -1):
		array = __max_heapify(array, i)
	return array

a = [5, 4, 1, 6, 10]
print(build_max_heap(a))

				
		



















				
		
	


