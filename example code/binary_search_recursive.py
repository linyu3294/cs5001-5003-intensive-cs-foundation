''' 
	CS5001 
	Spring 2019
	Lab 10 -- Recursive Binary Search
	Sample Solution 
'''
def regular_binary_search():
	''' 
		Function binary_search (iterative)
		Input: sorted list of elements to search, key to search for
		Returns: True if key found in A, False otherwise
	'''
	left = 0
	right = len(A) - 1
	while left <= right:
		midpoint = left + (right - left) // 2
		if A[midpoint] ==  key:
			return True
		elif A[midpoint] < key:
			left = midpoint + 1
		else:
			right = midpoint - 1
	return False
	

def recursive_binary_search (num, lst):
	left = 0
	right = len(lst) -1
	midpoint = left + (right - left) // 2
	
	print (lst[midpoint])
	print (lst)
	# base condition	
	if lst[midpoint] == num:
		print('a')
		return True
	elif left == right:
		print ('b')
		return False
	elif lst[midpoint] < num:
		print ('c')
		return(recursive_binary_search(num, lst[midpoint+1:] ))
	elif lst[midpoint] > num:
		print ('d')
		return(recursive_binary_search(num, lst[0: midpoint]))
	

	
	
	
def main():
	print (recursive_binary_search(1, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(2, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(15, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(21, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(38, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(43, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(79, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(94, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(97, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(32, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(14, [1,2,15,21,38,43,79,94]))
	print (recursive_binary_search(0, [1,2,15,21,38,43,79,94]))
main()
