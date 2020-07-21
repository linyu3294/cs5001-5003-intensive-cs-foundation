

'''   
   Yu Lin
   CS5001 - Spring 2019
   HW3 (List and Loops)
   Feb 1, 2019 
    
   My typed 100 words in 150.69 seconds
   My words per minute = 40
   My mismatches = 18
   My adjusted words per minute = 33
'''

import time
import random

PHRASES = [
           # My own sentences for testing		
           'Can we get some Love for Stephen Miller.',
           'Trump made a pretty good State of the Union Speech but did he write it?',	
           'What is the one horror movie that genuinely terrfied you while 	watching it. The decent was a pretty good movie.',	
           'My son stole a funny book from my brother. My brother is reluctant to take it back and is serious about it and wants to get the police involved. Can I get a break?'	,
           	'Last week my brother had a steak dinner but he was unwilling to share it with the rest of our family.',
           	'All this typing is making my hand really sore',
           	'What does it take to have enough upvotes to retire in the game of social media?',
           	
           # Original Sentences
           'Four Khoury faculty awarded Global Resilience Institute grants.',
           'Tired of being manipulated by fake news?',
           'One computer scientist’s strategies to improve data visualizations',
           'Now more than ever, computer science is everywhere.',
           'Prof. Manferdelli has been recognized for his work on the DSB.',
           'The work of the Defense Science Board has led to effective actions.',
           'Please take your dog, Cali, out for a walk; she needs exercise!',
           'What a beautiful day it is on the beach, here in sunny Hawaii.',
           'Dr. Quinfrey, a renowned scientist, made an invisibility machine.',
           'why are all those chemicals are so hazardous to the environment?',
           'The two kids collected twigs outside in the freezing cold!',
           'How many times have I told you? NEVER look at your race photos.',
           'Didn\'t see a moose, though. Come on, Maine.',
           'Yo minneapolis is cold',
            'Amazingly few discotheques provide jukeboxes!',
           'Jovial Debra Frantz swims quickly with grace and expertise.',
           'Six crazy kings vowed to abolish my quite pitiful jousts.',
           'Rex enjoys playing with farm ducks by the quiet lazy river?',
           'The five boxing wizards jumped quickly!',
           'The 116 saved 49 size 64 items for 26 friends going May 3',
           'Send 99 people to do 8 sets of 150 shows.',
           'The new school holds 3092 students; the older one, 568 more.',
           'He has seat 459 in car 985 of train 78, which is now at gate 31.',
           'The 36 men won 663 prizes in 52 games and 57 in 129 others.']

def select_sentence():
    ''' Function select_sentence
        Input: nothing
        Returns: a randomly-chosen sentence from the list above (string)
    '''
    return random.choice(PHRASES)

def count_words(sentence):
    ''' Function count_words
        Input: a string
        Returns: an int, the number of words in the given string.
                 Uses one white space as a delimiter, nothing else.
    '''
    words = sentence.split(' ')
    return len(words)

def count_mismatches(phrase_one, phrase_two):
    ''' Function count_mismatches
        Input: two strings for comparison
        Returns: an int, the number of differences between the two strings.
                 We count differences in each word (not each character).
                 If the words at position i in each sentence differ at ALL,
                 case included, that's a mismatch.
                 If one sentence is longer than the other, each extra word
                 it has is also a mismatch.
    '''
    list_one = phrase_one.split(' ')
    list_two = phrase_two.split(' ')
    min_length = min(len(list_one), len(list_two))

    # Count the position-by-position mismatches
    errors = 0
    for i in range(min_length):
        if list_one[i] != list_two[i]:
            errors += 1

    # Add on any mismatches if one phrase was longer
    errors += abs(len(list_one) - len(list_two))

    return errors
