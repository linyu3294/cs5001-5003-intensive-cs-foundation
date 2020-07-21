'''
   Yu Lin
   CS5001 - Spring 2019
   HW1 (Fuctions and Conditionals)
   Jan 17, 2019 
'''


def absolute(number):
    '''
       Name: absolute
       Input: a number (float or int)
       Returns: a number (float or int), the absolute value of the given input
    '''
    absolute_number = abs(number);
    return absolute_number


def manhattan (x1, y1, x2, y2):
    '''
       Name: manhattan
       Input: four numbers (float or int), representing coordinates (x1, y1, x2, y2)
       Returns: a float, the distance between the two coordinates
    '''
    right_angle_distance = absolute(x2 - x1) + absolute(y2 - y1)
    return right_angle_distance


def euclidean(x1, y1, x2, y2):
    '''
       Name: euclidean
       Input: four numbers (float or int), representing coordinates (x1, y1, x2, y2)
       Returns: a float, the distance between the two coordinates
    '''
    euclidean_distance = ((absolute(x2 - x1)  ** 2) + (absolute(y2 - y1) ** 2)) ** (0.5)
    return euclidean_distance
