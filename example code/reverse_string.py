'''
    CS5001
    Spring 2019
    Sample code from class -- writing code to reverse  a string
    Uses a stack class, and we test it with unittest code
'''

from mystack import Stack

def rev_string(string):
    ''' Function rev_string
        Params: string
        Returns: the reverse of the input string
    '''
    stack = Stack()
    rev = ""
    
    for letter in string:
        stack.push(letter)

    while not stack.is_empty():
        rev = rev + stack.top()
        stack.pop()

    return rev
