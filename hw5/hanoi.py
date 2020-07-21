'''
   Yu Lin
   CS5001 - Spring 2019
   HW5 (Recursion and Dictionary)
   Feb 19, 2019 
'''

from hanoi_viz import initialize_towers
from hanoi_viz import print_towers
from hanoi_viz import move_disk


def prompt_num_disks ():
	'''
		Function: prompt_num_disks
		Input: None
		Output: An Integer 
		Does: prompts the user to enter a number repeately until a valid number is entered. This number will be taken to set number of disks. 
	''' 
	while True:
		prompt = input('Enter the number of disks (integer between 1 and 8 (inclusive)' '\n')
		if prompt.isdigit():
			prompt = int(prompt)
			if 1 <= prompt and prompt <= 8:
				return prompt
			else: print ('Number Outside Range! Try Again')
		else: print ('Invalid Input! Try Again')

	
def move_tower (num_disks, orig, dest, temp, towers):
	if num_disks == 0:
		move_disk (orig, dest, towers)
	else:
		move_tower(num_disks - 1, orig, temp, dest, towers)
		move_disk (orig, dest, towers)
		move_tower(num_disks - 1, temp, dest, orig, towers)


def main():
	count = 0
	num_disks = prompt_num_disks()
	towers = initialize_towers(num_disks, 'A', 'B', 'C')
	move_tower (num_disks, 'A', 'B', 'C', towers)
main()
