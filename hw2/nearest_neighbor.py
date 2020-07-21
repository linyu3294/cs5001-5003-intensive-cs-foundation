
'''
   Yu Lin
   CS5001 - Spring 2019
   HW1 (Fuctions and Conditionals)
   Jan 17, 2019 
   
   Consulted Lab 2 work

     Test Case 1
     Your location (14, 52) 
     Expected Result : (Euclidean) You are closer to Starbucks
                       (Manhattan) You are closer to Starbucks

     Test Case 2
     Your location (-360, -43) 
     Expected Result : (Euclidean) You are closer to Dunkin
                       (Manhattan) You are closer to Dunkin

     Test Case 3
     Your location (-45.5, -58.4) 
     Expected Result : (Euclidean) You are closer to Dunkin
                       (Manhattan) You are closer to Dunkin
'''


import turtle
from distance import euclidean
from distance import manhattan

# Declare constants
Dunkin_x = 22.33
Dunkin_y = -173.09
Starbucks_x = 67.35
Starbucks_y = 71.18
Turt = turtle.Turtle()


def label (name, color, x_location, y_location):
    '''
        Function name:label
        Parameter(s): two strings (name and color of a lable on the Turtle canvas)
                      two numbers (coordinates of a lable on the Turtle canvas)
        Return: Nothing (the function will perform actions directly on the Turtle canvas)
    '''
    Turt.penup()
    Turt.goto(x_location, y_location)
    Turt.color(color)
    Turt.size = 100
    Turt.pendown()
    Turt.dot()
    Turt.penup()
    Turt.forward (10)
    Turt.write(name)
    Turt.goto(0, 0)
    return


def main ():
    # Draws the location of Dunkin and Starbucks respectively on the Turtle Canvas
    label ('Dunkin', 'red', Dunkin_x, Dunkin_y)
    label ('Starbucks', 'red', Starbucks_x, Starbucks_y)

    # Prompt to enter your x and y coordinates and combine as a single variable
    your_x = float (input("Enter your x coordinate \n"))
    your_y = float (input("Enter your y coordinate \n"))

    # Prompt to enter which distance to use Euclidean or Manhattan
    method = input("Enter which distance to use, euclidean or manhattan? \n")

    # Draws your location
    label('You', 'blue', your_x, your_y)

    # Figure out your distance from Dunkin and your distance from Starbucks
    if method == 'euclidean':
        distance_from_Dunkin = euclidean(your_x, your_y, Dunkin_x, Dunkin_y)
        distance_from_Starbucks = euclidean(your_x, your_y, Starbucks_x, Starbucks_y)
    if method == 'manhattan':
        distance_from_Dunkin = manhattan(your_x, your_y, Dunkin_x, Dunkin_y)
        distance_from_Starbucks = manhattan(your_x, your_y, Starbucks_x, Starbucks_y)

    # Determine if you are closer to Dunkin or Starbucks and print the result  
    if distance_from_Dunkin < distance_from_Starbucks:
        print('You are closer to Dunkin')
    if distance_from_Starbucks < distance_from_Dunkin:
        print('You are closer to Starbucks')
   
main()
