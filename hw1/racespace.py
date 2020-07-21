'''
    Yu Lin
    CS5001 - Spring 2019
    HW1 (Data Types and Arithmetic Operations)
    Jan 13, 2019


    Test cases
        
        Test case #1:
        153k race, 3 hour and 6 minute:
        95.03 miles, 1 min and 57 sec pace, 30.66 MPH

        Test case #2:
        95k race, 5 hours and 43 minutes:
        59.01 miles, 5 min and 48 sec pace, 10.32 MPH
        
        Test case #3:
        47k race, 2 hours and 27 minutes:
        29.19 miles, 5 min and 2 sec pace, 11.92 MPH
        
        Test case #3:
        225k race, 9 hours and 35 minutes:
        139.75 miles, 4 min and 6 sec pace, 14.58 MPH
        
        Test case #3:
        174k race, 6 hours and 59 minutes:
        108.07 miles, 3 min and 52 sec pace, 15.48 MPH
'''

import math



def main():



    # Part 1 Input
		
    # Prompt the user to input kilometers ran
    kmDist = float(input('What was the total distance of your race in kilometers?\n'))
    # Prompt the user to input number of hours
    hours = float(input('What is the hour component of your finish time (enter a whole number)\n'))
    # Prompt the user to input number of minutes
    minutes = float(input('What is the minute component of your finish time? (enter a whole number)\n'))
    

    
    # Part 2 calculations & Output
    
    # Store conversion unit as a contant 
    kmInMile = 1.61
    # Convert total distance in kilometers to distance in miles
    mileDist = (kmDist / kmInMile)
    # Output distance in miles
    print ('You ran', round (mileDist,2), 'miles \n')
    
    # Calculate the total time in minutes and save as a variable 
    totalMinutes = hours * 60 + minutes
    # Calculate the pace per minute
    pace = totalMinutes / mileDist
    # Output pace
    print ('Your pace:', 
           int(pace), 'min', 
           math.floor((pace % 1) *60) , 'sec per mile \n')
    
    # Calculate the total time in hours and save as a variable 
    totalHours = totalMinutes / 60
    # Calculate miles per hour
    mph = mileDist / totalHours
    # Output miles per hour
    print ('Your MPH:', round(mph, 2))


    
main()
