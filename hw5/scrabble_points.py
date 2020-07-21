'''   
   Yu Lin
   CS5001 - Spring 2019
   HW5 (Recursion and Dictionary)
   Feb 19, 2019
   Consulted Stackoverflow for instructions on how to do the following
   1) Take random number of items from a list and generate a new list (https://stackoverflow.com/questions/15511349/select-50-items-from-list-at-random-to-write-to-file)
   2) Index characters in a string (https://stackoverflow.com/questions/8848294/how-to-get-char-from-string-by-index)
'''

import random

def player_action ():
	'''
		 Name: get_menu
		 Params: None
		 Returns: A String, to indicate what action the player wants to do next 
		 Does: Displays and prompts user action
	'''
	user_commmands = ['d', 'D', 'w', 'W', 'p', 'P', 'q', 'Q']
	while True:
		action = str(input('\n' 'Player Actions (Type one of the Letters)' '\n'
												"'d'/'D'-- To Draw" '\n'
					 							"'w'/'W'-- To Make a Word from Letters in Play" '\n'
					 							"'p'/'P'-- To Print Player Stats" '\n'
					 							"'q'/'Q'-- To Quite Game" '\n' '\n'))
		if action in user_commmands:
			return action
		else: print ('Invalid Input! Try Again')
		


def bag_of_letters (frequency):
	'''
	 	 Params: dictionary where key = letter and value = frequency of that letter. 
   	 Returns: a list of letters, with each one repeated      according to its frequency.
   	 Example Input: {'A':1, 'B':2}. Expected output: 	['A', 'B', 'B']
	'''
	bag_of_letters = []
	for key in frequency:
		for i in range(frequency.get(key)):
		  bag_of_letters.append(key)    
	return bag_of_letters
	
	
	
def get_word_value (word, reward_table):
	word_points = 0
	'''
		 Params: a word to evaluate (string), and a dictionary where key = letter and value = points that letter is worth.
	 	 Returns: the total point value of the word (an int). If any letter in the word does not appear in the letter-value mapping, then return 0 points.
	 	 Example Inputs: 'HI', {'H':4, 'I':1}. Expected output: 5
	 	 Example Inputs: 'HELLO', {'H':4, 'I':1}. Expected output: 0
	'''	
	for i in range(len(word)):
		letter = word[i].upper()
		for key in reward_table:
			if letter == key:
				word_points = word_points + reward_table.get(key)
	return word_points
	
	
	
def is_valid_word (word, wordlist):
	'''
		 Name: is_valid_word
		 Params: a string : word played and a list: of valid words
		 returns: a boolean: indicating the validity of word played is true or false 
	'''
	return word.upper() in wordlist
	
	
	
def eval_word(word, letters_in_play, bag_of_letters, reward_table):
	'''Name: make_words
		 Parameters: A list: letters_in_play, another list: bag_of_letters, a string: word, a dictionary of rewards
		 Returns: Two updated lists: letters_in_play and bag of letter
		 Does: if word is played and is valid / earns points, update lists (letters_in_play, bag_of_letters)
	'''
	if get_word_value(word, reward_table) > 0:
			for i in range(len(word)):
				letters_in_play.remove(word[i].upper())
			
			replacement_letters = random.sample(bag_of_letters, len(word))
			for val in replacement_letters:
				bag_of_letters.remove(val)
				letters_in_play.append(val)
		
	return letters_in_play, bag_of_letters



def update_player_stats (word, word_points, player_stats):
	'''
		 Name: update_player_stats
		 Params: A string: a submitted word, A integer: points earned on a word, and a dictionary: where key = submitted words and value = points that each submitted word earned
		 returns: A dictionary: updated copy of the player_stats
	'''
	player_stats = player_stats.update({word : word_points})
	return player_stats 
	
	
def print_player_stats (player_stats):
	'''
		 Name: print_player_stats
		 Params: A dictionary: where key = submitted words and value = points that each submitted word earned
		 Returns: None 
		 Does: prints the player's current stats
	'''
	if bool(player_stats) :
		total_points = sum(player_stats.values())
		print ('\n' 'You have a total of', total_points, 'points so far' )
		for key in player_stats:
			print (key, "--", player_stats.get(key), 'points')
	else:
		total_points = 0
		print ('\n' 'You have a total of', total_points, 'points so far' '\n')
	
		
	return


def draw_seven_letters(letters_in_play, bag_of_letters):
	'''
	 	 Name: draw_seven_letters
	 	 Params: A list: letters_in_play, another list: bag_of_letters
	 	 Returns: A list: letters_in_play, another list: bag_of_letters 
	'''	
	replacement_letters = random.sample(bag_of_letters, 7)
	for val in replacement_letters:
		bag_of_letters.remove(val)
	letters_in_play = replacement_letters
	return letters_in_play, bag_of_letters
