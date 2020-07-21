'''
   Yu Lin
   CS5001 - Spring 2019
   HW1 (Fuctions and Conditionals)
   Jan 17, 2019 
'''
from distance import manhattan
from distance import absolute
from distance import euclidean

EPSILON = .0001

def test_absolute():
    ''' function test_absolute
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on absolute function, makes sure each absolute value output is as-expected.
    '''
    
    print ('\n \n' 'Running Absolute Test')
    num_failed = 0

    # Test 1: -9
    # Absolute value should be 9.0
    actual = absolute(-9)
    expected = 9.0
    print('Input (-9).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 2: 35
    # Absolute value should be 35.0
    actual = absolute(35)
    expected = 35.0
    print('Input (35).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1

    # Test 3: -13.7
    # Absolute value should be 13.7
    actual = absolute(-13.7)
    expected = 13.7
    print('Input (-13.7).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    # Test 4: 45.3
    # Absolute value should be 45.3
    actual = absolute(45.3)
    expected = 45.3
    print('Input (45.3).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    # Test 5: 0
    # Absolute value should be 0
    actual = absolute(0)
    expected = 0
    print('Input (0).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    return num_failed
        
        
        
def test_manhattan():
    ''' function test_manhattan
        Input: none
        Returns: int, # of tests that failed
        Does: tests a few different inputs on manhattan function, makes sure each manhattan distance value output is as-expected.
    '''
    
    print ('\n \n' 'Running Manhattan Test')
    num_failed = 0

    # Test 1: (0, 0), (0, 0)
    # Manhattan output value should be 0
    actual = manhattan(0, 0, 0, 0)
    expected = 0.0
    print('Input ((0, 0), (0, 0)).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 2: (8.4, 1.2), (-7.3, 26)
    # Manhattan output value should be 40.5
    actual = manhattan(8.4, 1.2, -7.3, 26)
    expected = 40.5
    print('Input ((8.4, 1.2), (-7.3, 26)).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 3: (-34, -23.9), (6.24, -54.138)
    # Manhattan output value should be 70.478
    actual = manhattan (-34, -23.9, 6.24, -54.138)
    expected = 70.478
    print('Input ((-34, -23.9), (6.24, -54.138)).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    # Test 4: (1, 3), (1, 3)
    # Manhattan output value should be 0.0
    actual = manhattan (1, 3, 1, 3)
    expected = 0.0
    print('Input ((1, 3), (1, 3)).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
    
    # Test 5: (9.72, -45.8), (- 13.6, -67.2)
    # Manhattan output value should be 44.72
    actual = manhattan(9.72, -45.8, - 13.6, -67.2)
    expected = 44.72
    print('Input ((9.72, -45.8), (- 13.6, -67.2)).\n'
          'Expected result', expected,
          'and actual result =', actual)
    if absolute(actual - expected) < EPSILON:
        print('SUCCESS!\n')
    else:
        print('FAIL :( \n')
        num_failed += 1
        
    return num_failed
        
        
        
    
def main():
		# Run test to test absolute function
    num_fail = test_absolute()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')
        
        
        
    # Run test to test manhattan function
    num_fail = test_manhattan()
    if num_fail == 0:
        print('ALL TESTS PASSED!')
    else:
        print('Sorry', num_fail, 'tests failed. Please go back and fix.')
       
main()
