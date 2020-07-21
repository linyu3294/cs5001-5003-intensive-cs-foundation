'''   
   Yu Lin
   CS5001 - Spring 2019
   HW3 (List and Loops)
   Feb 1, 2019 
'''

import random

def main ():
	# Set up initial variables
	points = [0, 0]
	turn_control = 0
	index = 0

	# prompt the two players to take turns and roll until someone has won
	while points[0]<20 and points [1]<20:
		# figures out whose turn it is and prompts player action
		index = turn_control % 2
		print ('\nPlayer', index+1, "it's your turn.\n")
		user_input = str (input ( "Would you like to roll or end turn? (Type 'r/R' to keep rolling or 'h/H' to end turn)"))
	
		if user_input.upper() == "R":
			dice_value = random.randint(1 , 6)
			
			# if palyer rolls 1, turn ends
			if dice_value == 1:
					points [index] = 0
					turn_control += 1
					print ("\nSorry, You rolled a 1. Your turn has ended!")
					
			else:	
					points [index] = points [index] + dice_value
					print ('\nPlayer', index+1, 'You got a', dice_value, 'on you current roll')
					print ('\nYour total points are', points [index], '\n')	
	
		elif user_input.upper() == "H":
			turn_control += 1
			
		else: print ("User input is invalid. Try Again!")
	
	print ('Player', index+1, ", YOU WON THE GAME! CONGRATS!")
main()
	
		




