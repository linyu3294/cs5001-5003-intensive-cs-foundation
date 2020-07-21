'''
    CS5001
    Spring 2019
    Sample code --- test the recursive version of some stuff
'''

from recursion import *

def test_get_max(lst, expected):
    ''' Function test_get_max
        Params: lst of ints to find the max in, expected result
        Returns: boolean indicating pass/fail
    '''
    print('Testing input list', lst, 'expected output', expected)
    if get_max(lst) == expected:
        print('SUCCESS!\n')
        return True
    print('FAIL :(\n')
    return False

def test_get_sum(lst, expected):
    ''' Function test_get_sum
        Params: lst of ints to find the sum of, expected result
        Returns: boolean indicating pass/fail
    '''
    print('Testing input list', lst, 'expected output', expected)
    if sum_list(lst) == expected:
        print('SUCCESS!\n')
        return True
    print('FAIL :(\n')
    return False

def test_is_in_list(lst, item, expected):
    ''' Function test_is_in_list
        Params: lst of ints, item to search for, expected result
        Returns: boolean indicating pass/fail
    '''
    print('Testing input list', lst, 'item', item, 'and expected output',
          expected)
    if is_in_list(lst, item) == expected:
        print('SUCCESS!\n')
        return True
    print('FAIL :(\n')
    return False


def run_max_tests():
    ''' Function: run_max_tests
        Params: none
        Returns: int, number of tests that failed
    '''
    num_fail = 0

    # Test One: List of size one, return the element
    if not test_get_max([4], 4):
        num_fail += 1

    # Test Two: List with two elements the same value, return one of them
    if not test_get_max([5, 5], 5):
        num_fail += 1

    # Test Three: Longer list w/8 elements, in ascending order
    if not test_get_max([-1, 0, 2, 5, 8, 10, 15, 16], 16):
        num_fail += 1

    # Test Four: Longer list w/8 elements, in descending order
    if not test_get_max([10, 0, -1, -5, -6, -7 -12, -20], 10):
        num_fail += 1

    # Test Five: mixed order with all positive integers
    if not test_get_max([7, 4, 3, 0, 15, 4, 7, 200, 12], 200):
        num_fail += 1

    return num_fail

def run_sum_tests():
    ''' Function: run_sum_tests
        Params: none
        Returns: int, number of tests that failed
    '''
    num_fail = 0

    # Test One: List of size one, sum is the single element
    if not test_get_sum([4], 4):
        num_fail += 1

    # Test Two: List with two elements, sum is them both together
    if not test_get_sum([5, 5], 10):
        num_fail += 1

    # Test Three: Longer list, in ascending order
    if not test_get_sum([10, 15, 16], 41):
        num_fail += 1

    # Test Four: Longer list w/8 elements, in descending order
    if not test_get_sum([10, 0, -1, -5, -6, -7 -12, -20], -41):
        num_fail += 1

    # Test Five: mixed order with all positive integers
    if not test_get_sum([7, 4, 3, 0, 15, 4, 7, 200, 12], 252):
        num_fail += 1

    # Test Six: all zeroes
    if not test_get_sum([0, 0, 0], 0):
        num_fail += 1

    return num_fail

def run_search_tests():
    ''' Function: run_search_tests
        Params: none
        Returns: int, number of tests that failed
    '''
    num_fail = 0

    # Test One: List of size one, look for that element, it's there
    if not test_is_in_list([4], 4, True):
        num_fail += 1

    # Test Two: List of size one, look for that element, it's not there
    if not test_is_in_list([4], 5, False):
        num_fail += 1
        
    # Test Two: List with two elements, one is there
    if not test_is_in_list([5, 18], 5, True):
        num_fail += 1

    # Test Three: Longer list, item not there
    if not test_is_in_list([10, 15, 16, -1, -8, 0, 5, 13, 12], 3, False):
        num_fail += 1

    # Test Four: Longer list with repeated elements, item is there
    if not test_is_in_list([10, 0, -1, -1, 6, -7, 6, 6], 6, True):
        num_fail += 1

    # Test Five: all zeroes, item not there
    if not test_is_in_list([0, 0, 0, 0, 0], 18, False):
        num_fail += 1

    return num_fail

def run_sum_tests():
    ''' Function: run_sum_tests
        Params: none
        Returns: int, number of tests that failed
    '''
    num_fail = 0

    # Test One: List of size one, sum is the single element
    if not test_get_sum([4], 4):
        num_fail += 1

    # Test Two: List with two elements, sum is them both together
    if not test_get_sum([5, 5], 10):
        num_fail += 1

    # Test Three: Longer list, in ascending order
    if not test_get_sum([10, 15, 16], 41):
        num_fail += 1

    # Test Four: Longer list w/8 elements, in descending order
    if not test_get_sum([10, 0, -1, -5, -6, -7 -12, -20], -41):
        num_fail += 1

    # Test Five: mixed order with all positive integers
    if not test_get_sum([7, 4, 3, 0, 15, 4, 7, 200, 12], 252):
        num_fail += 1

    # Test Six: all zeroes
    if not test_get_sum([0, 0, 0], 0):
        num_fail += 1

    return num_fail


def main():
    # We have three tests to run, and we let the user choose
    # which one(s) to execute: get_max, get_sum, and is_in_list

    # Test group 1 -- get_max
    user_input = input('Run the get_max tests? Enter Y/N.\n')
    if user_input == 'Y':
        print('testing the get_max function...')
        num_failed = run_max_tests()
        if num_failed == 0:
            print('All get max tests passed!\n')
        else:
            print('Something broke in get_max, fix pls.\n')

    # Test group 2 -- get_sum
    user_input = input('Run the get_sum tests? Enter Y/N.\n')
    if user_input == 'Y':
        print('testing the sum_list function...')
        num_failed = run_sum_tests()
        if num_failed == 0:
            print('All get sum tests passed!\n')
        else:
            print('Something broke in get_max, fix pls.\n')

    # Test group 3 -- is_in_list
    user_input = input('Run the is_in_list tests? Enter Y/N.\n')
    if user_input == 'Y':
        print('testing the is_in_list function...')
        num_failed = run_search_tests()
        if num_failed == 0:
            print('All get search tests passed!\n')
        else:
            print('Something broke in get_max, fix pls.\n')

    # Test group 4 -- see what spam does
    user_input = input('Want to see what the mystery spam function does?\n')
    if user_input == 'Y':
        print('Calling spam on [4, 5, 6, 7, 8]')
        spam([4, 5, 6, 7, 8])

        print('\nCalling spam on [2]')
        spam([2])

        print('\nCalling spam on [1, 1, 2, 3, 5, 8, 13]')
        spam([1, 1, 2, 3, 5, 8, 13])
    

main()
