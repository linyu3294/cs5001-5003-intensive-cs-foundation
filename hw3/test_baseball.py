'''   
   Yu Lin
   CS5001 - Spring 2019
   HW3 (List and Loops)
   Feb 1, 2019 
'''


from baseball import calc_wins_losses
from baseball import calc_avg_runs
from baseball import calc_winners
from baseball import calc_losers

EPSILON = .0001

def test_calc_wins_losses():
    ''' function: test_calc_wins_losses
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on calc_wins_losses function, makes sure each output is as-expected.
    '''
    
    print ('\n \n' 'Running calc_wins_losses Test')
    num_failed = 0

    # Test 1: ['W', 'W', 'L', 'W', 'L', 'L', 'L', 'W']
    # Output value should be [4, 4]
    actual = calc_wins_losses (['W', 'W', 'L', 'W', 'L', 'L', 'L', 'W'])
    expected = [4, 4]
    print("Input 'W', 'W', 'L', 'W', 'L', 'L', 'L', 'W'.\n"
          'Expected result', expected,
          'and actual result =', actual)
    if expected == actual:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 2: ['W', 'W', 'L', 'W', 'L', 'L', 'L', 'L', 'W', 'L', 'L', 'W']
    # Output value should be [5, 7]
    actual = calc_wins_losses (['W', 'W', 'L', 'W', 'L', 'L', 'L', 'L', 'W', 'L', 'L', 'W'])
    expected = [5, 7]
    print("Input ['W', 'W', 'L', 'W', 'L', 'L', 'L', 'L', 'W', 'L', 'L', 'W'].\n"
          'Expected result', expected,
          'and actual result =', actual)
    if expected == actual:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    # Test 3: ['W']
    # Output value should be [1, 0]
    actual = calc_wins_losses (['W'])
    expected = [1, 0]
    print("Input ['W'].\n"
          'Expected result', expected,
          'and actual result =', actual)
    if expected == actual:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
       
    # Test 4: ['L']
    # Output value should be [0, 1]
    actual = calc_wins_losses (['L'])
    expected = [0, 1]
    print("Input ['L'].\n"
          'Expected result', expected,
          'and actual result =', actual)
    if expected == actual:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    return num_failed
        
  
              

def test_calc_avg_runs():
    ''' function: test_calc_avg_runs
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on calc_avg_runs function, makes sure each output is as-expected.
    '''
    
    print ('\n \n' 'Running calc_avg_runs Test')
    num_failed = 0
    
    # Test 1: [2, 4, 5, 1, 10, 3, 5]
    # Output value should be 4.29
    actual = float (calc_avg_runs ([2, 4, 5, 1, 10, 3, 5]))
    expected = 4.29
    print("Input [2, 4, 5, 1, 10, 3, 5].\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    
    # Test 2: [1, 2, 4, 12, 4, 7, 14, 0, 2, 23, 19]
    # Output value should be 8.00
    actual = float (calc_avg_runs ([1, 2, 4, 12, 4, 7, 14, 0, 2, 23, 19]))
    expected = 8.00
    print("Input [1, 2, 4, 12, 4, 7, 14, 0, 2, 23, 19].\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    # Test 3: [0]
    # Output value should be 0.00
    actual = float (calc_avg_runs ([0]))
    expected = 0.00
    print("Input [0].\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 4: [2, 5, 6, 8, 3, 5, 7]
    # Output value should be 5.14
    actual = float (calc_avg_runs ([2, 5, 6, 8, 3, 5, 7]))
    expected = 5.14
    print("Input [2, 5, 6, 8, 3, 5, 7].\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    
    return num_failed




def test_calc_winners():
    ''' function: test_calc_winners
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on calc_winners function, makes sure each output is as-expected.
    '''
    
    print ('\n \n' 'Running calc_winners Test')
    num_failed = 0

    # Test 1: ['W', 'L', 'L', 'W', 'L', 'W', 'L'] , [1, 5, 6, 8, 3, 1, 7], 1 
    # Output value should be 2
    actual = calc_winners (['W', 'L', 'L', 'W', 'L', 'W', 'L'] , [1, 5, 6, 8, 3, 1, 7], 1 )
    expected = 2
    print("Input ['W', 'L', 'L', 'W', 'L', 'W', 'L'] , [1, 5, 6, 8, 3, 1, 7], 1 .\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
        
    # Test 2: ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [0, 3, 1, 2, 5, 8, 4, 1, 1, 0, 1], 1 
    # Output value should be 3
    actual = calc_winners (['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [0, 3, 1, 2, 5, 8, 4, 1, 1, 0, 1], 1)
    expected = 3
    print("Input ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [0, 3, 1, 2, 5, 8, 4, 1, 1, 0, 1], 1.\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
        
    # Test 3: ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 4 
    # Output value should be 5
    actual = calc_winners (['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 4)
    expected = 5
    print("Input  ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 4 .\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    
    # Test 3: ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 2 
    # Output value should be 0
    actual = calc_winners (['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 2)
    expected = 0
    print("Input  ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 2 .\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    return num_failed


		
def test_calc_losers():
    ''' function: test_calc_losers
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on calc_losers function, makes sure each output is as-expected.
    '''
    
    print ('\n \n' 'Running calc_losers Test')
    num_failed = 0

    # Test 1: ['W', 'L', 'L', 'W', 'L', 'W', 'L'] , [1, 5, 6, 8, 3, 1, 7], 1 
    # Output value should be 1
    actual = calc_losers (['W', 'L', 'L', 'W', 'L', 'W', 'L'] , [1, 5, 6, 8, 3, 1, 7], 7 )
    expected = 1
    print("Input ['W', 'L', 'L', 'W', 'L', 'W', 'L'] , [1, 5, 6, 8, 3, 1, 7], 7 .\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
        
    # Test 2: ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [0, 3, 1, 2, 5, 8, 4, 1, 1, 0, 1], 4
    # Output value should be 2
    actual = calc_losers (['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [0, 3, 1, 2, 5, 8, 4, 1, 1, 0, 1], 4)
    expected = 2
    print("Input ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [0, 3, 1, 2, 5, 8, 4, 1, 1, 0, 1], 4.\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
        
    # Test 3: ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 12 
    # Output value should be 0
    actual = calc_losers (['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 12)
    expected = 0
    print("Input  ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 3, 4, 4, 5, 8, 4, 1, 4, 4, 1], 12 .\n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    
    # Test 4: ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 6, 4, 7, 5, 8, 4, 1, 4, 4, 1], 6 
    # Output value should be 3
    actual = calc_losers (['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'] , [4, 6, 4, 7, 5, 8, 4, 1, 4, 4, 1], 6)
    expected = 3
    print("Input  ['W', 'L', 'W', 'L', 'L', 'L', 'W', 'L', 'W', 'W', 'W'], [4, 6, 4, 7, 5, 8, 4, 1, 4, 4, 1], 6  \n"
          'Expected result', expected,
          'and actual result =', actual)
    diff = actual - expected
    if abs(diff) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    return num_failed



    
    
    
    
    
def main():
		# Run test to test calc_wins_losses function
    num_fail = test_calc_wins_losses()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')
        
    # Run test to test calc_avg_runs function
    num_fail = test_calc_avg_runs()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')  
        
    # Run test to test calc_winners function
    num_fail = test_calc_winners()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')  
        
    # Run test to test calc_losers function
    num_fail = test_calc_losers()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.') 
       
main()
