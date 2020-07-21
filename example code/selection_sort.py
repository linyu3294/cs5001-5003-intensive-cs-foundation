'''
    CS5001
    Spring 2019
    Selection sort
'''

def selection_sort(A):
    ''' input A, unsorted list of anything
        returns: nothing, modifies the list
    '''
    for i in range(len(A)):
        curr_min = A[i]
        curr_min_pos = i
        for j in range(i + 1, len(A)):
            if A[j] < curr_min:
                curr_min = A[j]
                curr_min_pos = j
        temp = A[i]
        A[i] = A[curr_min_pos]
        A[curr_min_pos] = temp
        
