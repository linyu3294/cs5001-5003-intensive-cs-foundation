'''   
   Yu Lin
   CS5001 - Spring 2019
   HW5 (Recursion and Dictionary)
   Feb 19, 2019 
   
   consulted the following url to look up alphabet iteration : https://stackoverflow.com/questions/16060899/alphabet-range-python/31888217 
   consulted the following url to look up returning multiple variables in a function : https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
'''


from wordlist import get_wordlist
from scrabble_points import player_action
from scrabble_points import bag_of_letters
from scrabble_points import get_word_value
from scrabble_points import is_valid_word
from scrabble_points import eval_word
from scrabble_points import update_player_stats
from scrabble_points import print_player_stats
from scrabble_points import draw_seven_letters



WORDLIST = []
for value in get_wordlist():
	WORDLIST.append(value.upper())
	
REWARD_TABLE = {'A': 1,'B': 3,'C': 3,'D': 2,'E': 1,'F': 4,
								'G': 2,'H': 4,'I': 1,'J': 8,'K': 5,'L': 1,
								'M': 3,'N': 1,'O': 1,'P': 3,'Q': 10,'R':1,
								'S': 1,'T': 1,'U': 1,'V': 4,'W': 4,'X': 8,
								'Y': 4,'Z': 10}
	
def assemble_bag ():
	'''
		 Name: assemble_bag
		 Params: None
		 Returns: initial composition of letters in the start the game
	'''
	bag = bag_of_letters ({'A': 9,'B': 2,'C': 2,'D': 4,'E': 12,'F': 2,
												 'G': 3,'H': 2,'I': 9,'J': 1,'K': 1,'L': 4,
									 			 'M': 2,'N': 6,'O': 8,'P': 2,'Q': 1,'R': 6,
												 'S': 4,'T': 6,'U': 4,'V':2 ,'W': 2,'X': 1,
									 			 'Y': 2,'Z': 1, "_": 2})
	return bag
	
	
	
	

		
def main():
	total_points = 0
	player_stats = {}
	letters_in_play = []
	bag = assemble_bag()
	letters_in_play, bag = draw_seven_letters(letters_in_play, bag)
	print ('letters in play:', letters_in_play)
	
	while True:	
		action = player_action()
		if action == 'D' or action == 'd':
			letters_in_play, bag = draw_seven_letters(letters_in_play, bag)
			print ('letters in play:', letters_in_play)
		elif action == 'P' or action == 'p':
			print_player_stats (player_stats)
			print ('letters in play:', letters_in_play)
		elif action == 'W' or action == 'w':
			print ('letters in play:', letters_in_play)
			word = str(input('Enter letters from your letters in play to make a word' '\n'))
			if is_valid_word (word, WORDLIST):
				letters_in_play, bag = eval_word (word, letters_in_play, bag, REWARD_TABLE)
				word_points = get_word_value (word, REWARD_TABLE)
				total_points = total_points + word_points
				player_stats [word] = word_points
		elif action == 'Q' or action == 'q':
			break
		
	
	
main()
