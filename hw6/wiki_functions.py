'''
	Yu Lin
	CS5001 (Intensive Foundations)
	Homework 6 (Files And Exceptions)
	March 18, 2019
'''

import os

def prompt_menu() : 
	command = ''
	while command not in ['F','C','E','K', 'Q']:
		command = input ('\n' 'Choose from one of the following options. \n'
			'F -- Input Filename \n'
			'C -- Count revisions \n'
			'E -- Top n Editors \n'
			'K -- Search comments \n'
			'Q -- Quit \n'
			'Enter your choice now. \n')
	return command
	

	
def input_filename ():
	''' 
			Function: input_filename
			Params: None
		 	Returns: Valid Filename entered by User
		 	Does: Checks to make sure that file exists in the same directory as the Python Program, repeatedly re-prompt until they enter a valid filename
	'''
	stay_in_loop = True
	while stay_in_loop:	
		try:
			filename = input('\n' 'Enter the name of the file \n')
			if os.path.exists(filename):
				stay_in_loop = False
				print ('Ok, using', filename)
				return filename
			else:	
				print('The file entered was does not exist in the program directory, please try again! \n')
		except OSError:
				print ('Oops there is an error when verifying the your file path exist. Make sure your typing is correct!')
			

	
def count_revisions(filename):
	'''
		Function: count_revisions
		Params: filename (a string)
		Returns: Number of revisions (a integer)
	  Does: Counts the number of revision documented
	  			in a file and returns it as an integer
	'''
	try:
		infile = open(filename, 'r')
		all_data = infile.read()
		lines = all_data.splitlines()
		count = 0
		for line in lines:
			if 'REVISION' in line:
				count += 1
		infile.close()
		print ('There are', count, 'revisions in the file', filename)
	except OSError:
		print ('Oops there is an error when opening your file. Make sure you input the file first!')
	return count
	
	
	
def top_n_editors(filename):
	'''	
		Function: top_n_editors
		Parameters: filename (a string)
		returns : returns Nothing 
		Does: prints the top tier editors, the size of which is controlled by a user prompt (is the parent function to two children functions, catalog() and get_top_editors() )
	'''
	# prompt user to enter the number of top editors to look up
	try: 
		number_of_editors = int (input('\n''How many editors?''\n'))
		if number_of_editors <= 0:
			number_of_editors = 1
	except ValueError:
		# do if user enters a non-integer
		number_of_editors = 1
		
	# initiate and create a list for all revisions' editors in the file (will contain reoccurences)		
	all_editors_lst = []
	try:
		infile = open(filename, 'r')
		all_data = infile.read()
		lines =  all_data.splitlines()
		for line in lines:
			if 'REVISION' in line: 
				all_editors_lst.append(line.split() [-2])
		
		# counts revisions and creates dictionary (editor : # of revision)
		all_editors_dictionary = catalog (all_editors_lst)
		
		# truncates the previous dictionary to user-specified size
		top_editors_dictionary = get_top_editors (all_editors_dictionary, number_of_editors)	
		
		infile.close()
		
		# prints the result
		print ('\n' 'The top editors are...' '\n')
		for key, val in top_editors_dictionary.items():
			print (key, '--', val, '\n')
			
	except OSError:
		print ('Oops there is an error when opening your file. Make sure you input the file first!')
	return 
	


def catalog (all_editors_lst):
	'''
		Function: catalog
		Params: a list of authors for every instance of revision (length of list == the number of revision)
		returns: a dictionary 
		does: counts the number instance for each author and saves in a dictionary (key == author, value == number revision )
	'''
	
	all_editors_dictionary = {}
	for item in all_editors_lst:
		if item in all_editors_dictionary:
			all_editors_dictionary [item] = all_editors_dictionary.get(item) + 1
		else:
			all_editors_dictionary [item] = 1
	return all_editors_dictionary




def get_top_editors (all_editors_dictionary, number_of_editors):
	'''
		Function: top_values
		Params: dictionary(contains all editor names as keys and their respective entries as values), a integer (number of editors to be included into a new top_editors dictionary)
		returns: a top_editors_dictionary (a dictionary that contains only editors in the top tier)
		Does: trucates and transforms all_editors_dictionary into top_editors_dictionary
	'''
	
		
	# do if user enters an integer greater than the number of editors 
	if number_of_editors >= len(all_editors_dictionary):
			return all_editors_dictionary
	
	# do if user enters a valid integer
	if number_of_editors < len(all_editors_dictionary):		
		# Initiate Local variables
		revisions_lst = []
		top_editors_dictionary = {}
	
		# Extract values in all_editors_dictionary call it revision_lst
		# Sort throuh revision_lst
		revisions_lst = list(all_editors_dictionary.values())		
		revisions_lst = sorted(revisions_lst, reverse = True)

		# Compile top_editors_dictionary from all_editors_dictionary
		for i in range(number_of_editors):
			for key in all_editors_dictionary:
				if revisions_lst [i] == all_editors_dictionary.get(key) and key not in top_editors_dictionary: 
					top_editors_dictionary [key] = all_editors_dictionary.get(key)
					break
		return top_editors_dictionary 
				
	
def search_comments (filename):
	'''
		Function: search_comments
		Params: a string (filename)
		Returns: Nothing
		Does: prompt user to enter a keyword and print out all the comments that contain it and associated ids
	'''
	count = 0
	search_word = input('\n''Type word to search for in comments?''\n')
	try:
		infile = open(filename,'r')
		all_data = infile.read()
		entries = all_data.split('REVISION')
		for entry in entries:
			lines = entry.splitlines()
			for line in lines:
				if 'COMMENT' in line and search_word in line:
					print (lines[0].split()[0], line.replace('COMMENT', '--'))
					count += 1
		infile.close()
		if count == 0:
			print('No comments were found with that word.' '\n')			
	except OSError:
		print ('Oops there is an error when opening your file. Make sure you input the file first!')
	return


def quit ():	
	return
