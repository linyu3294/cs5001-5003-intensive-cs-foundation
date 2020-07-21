'''
    CS5001
    Bianry search
'''

'''
 A = [8, 12, 13, 15, 19, 20, 22]
 pos  0   1   2  3   4   5   6

key = 13

leftmost = 0
rightmost = 6
midpoint = 3

A[3] == 13 ?

discard right half

list we care about: [8, 12, 13]
                     0   1  2

leftmost = 0
rightmost = 2
2 + 0 // 2 .... 1

midpoint = 1



A[1] == 13?
dicsard left half

list we care about: [13]

midpoint = 0
A[0] == 13??????
return True!

0 + 0 // 2....0




 A = [8, 12, 13, 15, 19, 20, 22]
 pos  0   1   2  3   4   5   6

 key = 22

 midpoint = 3
 A[3] == 22??

discard left half, keep seraching in the right

list we care about: [19, 20, 22]
                     4    5   6

leftmost = 4
rightmost = 6
(6 + 4) // 2...5

midpoint = 5
A[5] == 22???

discard left half, keep searching in the right

list we care about: [22]
                      6


midpoint =  (6 + 6) // 2...6


A[6] == 22?????
Return True!!!!!!
 
'''


 
def binary_search(A, key):
    ''' A is a sorted list, key is element we're looking for '''

    # calculate the midpoint of the list
    # midpoint = (position in middle of the list)
    left = 0
    right = len(A) - 1
    
    while left <= right:
        midpoint = (left + right) // 2        
                
        if A[midpoint] == key:
            return True
        elif A[midpoint] < key:
            # throw away left half
            # continue search in right half
            left = midpoint + 1
        else:
            # throw away right half
            # continue searching in left half
            right = midpoint - 1

    return False
