'''
    CS5001
    Spring 2019
    Errors, with and without exceptions
'''

def file_error():
    print('DEMO: Opening a non-existent file for reading.\n')

    # Attempt #1, use an exception to handle gracefully
    print('With exceptions...')    
    try:
        infile = open('nonfile.txt', 'r')
        file_values = infile.read()
        infile.close()
    except OSError:
        print('Could not read from file!')

    # Attempt #2, don't use an exception and it's gross
    print('\nAnd without...')
    infile = open('nonfile.txt', 'r')
    
        
def value_error():
    print('DEMO: Expect an integer, user gives you a string\n')

    # Attempt #1, use an exception to handle gracefully
    print('With exceptions...')
    try:
        x = int(input('Enter an integer\n'))
    except ValueError:
        print('That\'s not an integer!!!')

    # Attempt #2, don't use an exception and it's gross
    print('\nAnd without...')
    x = int(input('Enter an integer\n'))


def type_error():
    print('DEMO: Perform an operation on the wrong data type\n')

    # Attempt #1, use an exception to handle gracefully
    print('With exceptions...')
    try:
        result = 'jello' / 'o'
    except TypeError:
        print('Could not do jello / o, sorry about that.')

    # Attempt #2, dont' use an exception and it's gross
    print('\nAnd without...')
    result = 'jello' / 'o'

def index_error():
    print('DEMO: Try to read outside the bounds of a list\n')

    # Attempt #1, use an exception to handle gracefully
    print('With exceptions...')
    lst = [1, 2, 3]
    try:
        lst[18] = 0
    except IndexError:
        print('Could not access position 18 in that list')

    print('\nAnd  without...')
    # Attempt #2, don't use an exception and it's gross
    lst[18] = 0
    

def main():
    functions = [file_error, value_error, type_error, index_error]
    print('Which error handling function do you want to call?')
    for i in range(len(functions)):
        print(i, ":", functions[i].__name__)
    func_index = int(input('Enter a number to choose\n'))

    functions[func_index]()

main()
    
    
