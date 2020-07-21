'''
   Yu Lin
   CS5001 - Spring 2019
   HW3 (List and Loops)
   Feb 1, 2019 
   
   
   Consulted the following website to learn new time expressions and operations (https://docs.python.org/2/library/time.html) 
'''


from sentence import select_sentence
from sentence import count_words
from sentence import count_mismatches
import time



def main ():
		# set up initial variables
		time_start = time.time()
		total_words = 0
		mismatches = 0
		begin_test = True
		
		# loop through random sentences for tester to type and breaks out the loop when tester types 'DONE'
		while begin_test :
			sentence = select_sentence ()
			print ('\n\n\n[Type the following sentence... OR type \'DONE\' to quit]\n\n' + sentence)
			sentence_input = str (input ("\n"))
			if sentence_input == "DONE":
				 break
			total_words = total_words + count_words (sentence_input)
			mismatches = mismatches + count_mismatches(sentence, sentence_input)
			
		# calculate tester's' stats
		time_end = time.time()
		total_seconds = time_end - time_start
		total_minutes = total_seconds / 60
		words_per_min = round (total_words / total_minutes)
		adjusted_words_per_min = round ((total_words - mismatches) / total_minutes)
			
		# reports tester's' stats	
		print ('\n\nYou typed', total_words ,'words in', float ('{:0.2f}'.format (total_seconds)), 'seconds')
		print ('Your words per minute =', words_per_min)
		print ('Your mismatches =', mismatches)
		print ('Your adjusted words per minute =', adjusted_words_per_min)
		
main () 

