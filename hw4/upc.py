'''   
   Yu Lin
   CS5001 - Spring 2019
   HW4 (List, Loops and Strings)
   Feb 10, 2019 
'''

EPSILON = .0001

def test_is_valid_upc (input, expected_output):
''' 
		function: test_is_valid_upc
		Input: 
			1) A test case input of is_valid_upc
			2) Expect result of is_valid_upc for the same test case
		Returns: int, # of tests that failed
		Does: tests one instance of input on is_valid_upc function, makes sure corresponding output is as-expected.
'''
		num_failed = 0
		# iput is passed in as a parameter
		# expected output is passed in as a parameter
		actual = is_valid_upc (input)
		print('Input', input, '.\n'
          'Expected result', expected,
          'and actual result =', actual)
		if expected_output == actual:
			print('SUCCESS!\n')
		else:
			print('FAIL :( \n')
      num_failed += 1
		return num_failed
	

def main():
	print ('\n \n' 'Running calc_wins_losses Test')
  num_failed = 0  
	num_failed = num_failed + test_is_valid_upc ('073854008089' , True)
	print (num_failed)
	
main()
