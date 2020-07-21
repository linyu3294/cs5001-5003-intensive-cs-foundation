'''   
	 Yu Lin
   CS5001 - Spring 2019
   HW5 (Recursion and Dictionary)
   Feb 1, 2019 
'''

# Recursive Functions

# Algorithm for log
def logger (inter):
	if inter == 1:
		return 0
	else:
		return 1 + logger(inter/2)
		
		
# Algorithm for Fibonacci Number	
def fibonacci (integer_in_Fib):
	if integer_in_Fib == 0:
		return 0
	if integer_in_Fib == 1:
		return 1
	else:
		return fibonacci(integer_in_Fib-1) +fibonacci (integer_in_Fib-2)
		
		
def get_max(lst):
    # base case
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = get_max(lst[1:])
        if max_of_rest > lst[0]:
            return max_of_rest
        else:
            return lst[0]


def sum_list(lst):
    ''' Function sum_list
        Params: list of any numbers
        Returns: the sum of all the elements in the list
        Does: recursively sums all the values
    '''
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])


def is_in_list(lst, key):
    ''' Function is_in_list
        Params: list of elements, key to search for
        Returns: True if key in list, False otherwise
    '''
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] == key or is_in_list(lst[1:], key)
        

def spam(lst):
    ''' Function: spam
        Params: list
        Returns: nothing, just prints.
        Does: ????????
    '''
    if len(lst) == 0:
       return
    else:
        spam(lst[1:])
        print(lst[0])

def factorial (n):
	'''	
		Name: factorial
		Parameter: n, a positive integer
		Returns: n!
	'''
	if n == 1:
		return 1
	else:
		return n * factorial (n-1)
		
		
def sum_list (lst, dict):
	if len(lst) > 0:
		if lst[0] in dict: 
			dict [lst[0]] = dict.get(lst[0]) + 1
		else:	
			dict [lst[0]] = 1
		sum_list (lst[1::], dict)
				



def main():
	print(logger(4))
	print(fibonacci(10))
	
	lst = ['Bob','Jon','Bob','Karen','Waldo','Jon','Kathy', 'James','Don','James','Bob','Robert']
	n =12
	dict = {}
	sum_list(lst, dict)
	print (dict)
main()
