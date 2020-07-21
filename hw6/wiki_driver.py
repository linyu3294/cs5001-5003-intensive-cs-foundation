'''
	Yu Lin
	CS5001 (Intensive Foundations)
	Homework 6 (Files And Exceptions)
	March 18, 2019
'''

from wiki_functions import prompt_menu
from wiki_functions import input_filename
from wiki_functions import count_revisions
from wiki_functions import top_n_editors
from wiki_functions import search_comments
from wiki_functions import quit


def main():
	filename = ''
	run = True
	while run:		
		user_input = prompt_menu()
		if user_input == 'F':
			filename = input_filename()
		if user_input == 'C':
			count_revisions(filename)
		if user_input == 'E':
			top_n_editors(filename)
		if user_input == 'K':
			search_comments(filename)
		if user_input == 'Q':
			break
main()
