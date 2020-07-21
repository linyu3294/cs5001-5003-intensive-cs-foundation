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
from wiki_functions import catalog
from wiki_functions import get_top_editors

class Function_Test:
	def __init__(self, expected_result, actual_result):
		self.expected = expected_result
		self.actual = actual_result
		self.pass_or_fail = ''

	def __get_outcome__ (self):
		if self.expected == self.actual:
			self.pass_or_fail = 'PASS' 
		else:
			self.pass_or_fail = 'FAIL'
		return self.pass_or_fail
			
	def __str__ (self):
		print ('Your Expected Result is [', self.expected, ']', '\n' 'Your Actual Result is [', self.actual, ']', '\n' 'Your Test Outcome is', self.__get_outcome__(), '\n' )
		
	# Skipping __eq__ cuz it would not make sense to have this function in a function test class

			
def main():
 successes = 0
 fails = 0
 
 print ('Now Testing Function: count_revisions()')	
 count_revisions_actual_result = count_revisions ('small_wiki.txt')
 count_revisions_test1 = Function_Test( 12, count_revisions_actual_result )
 count_revisions_test1.__str__()
 if count_revisions_test1.pass_or_fail == 'PASS':
 	successes +=1
 else:
 	fails += 1
 	
 	
 
 print ('Now Testing Function: catalog()')	
 catalog_actual_result1 = catalog (['Bob', 'Cathy', 'Sean', 'Jon', 'Cathy', 'Cathy'])
 catalog_test1 = Function_Test( catalog_actual_result1,  {'Cathy': 3, 'Jon' : 1, 'Bob': 1, 'Sean': 1} )
 catalog_test1.__str__()
 if catalog_test1.pass_or_fail == 'PASS':
 	successes +=1
 else:
 	fails += 1
 	
 	
 	
 print ('Now Testing Function: catalog() AGAIN!')	
 catalog_actual_result2 = catalog (['Nicole', 'Jean', 'Nicole', 'Don', 'Jean', 'Nathan', 'Nathan', 'Don', 'Nicole'])
 catalog_test2 = Function_Test( catalog_actual_result2,  {'Nicole': 3, 'Jean' : 2, 'Don': 2, 'Nathan': 2} )
 catalog_test2.__str__()
 if catalog_test2.pass_or_fail == 'PASS':
 	successes +=1
 else:
 	fails += 1
 
 
 
 print ('Now Testing Function: catalog() ONE MORE TIME!')	
 catalog_actual_result3 = catalog (['Nicole'])
 catalog_test3 = Function_Test( catalog_actual_result3,  {'Nicole': 1})
 catalog_test3.__str__()
 if catalog_test3.pass_or_fail == 'PASS':
 	successes +=1
 else:
 	fails += 1
 	
 	
 
 
 print ('Now Testing Function: get_top_editors()')	
 get_top_editors_actual_result1 = get_top_editors ({'Bob':1, 'Hannah': 7, 'Nicole': 2, 'Donny': 2, 'Jamie': 5, 'Tywin': 4}, 3)
 get_top_editors_test1 = Function_Test( {'Tywin':4, 'Hannah': 7, 'Jamie': 5}, get_top_editors_actual_result1)
 get_top_editors_test1.__str__()
 if get_top_editors_test1.pass_or_fail == 'PASS':
 	successes +=1
 else:
 	fails += 1
 
 
 
 print ('Now Testing Function: get_top_editors() AGAIN!')	
 get_top_editors_actual_result2 = get_top_editors ({'Bob':1, 'Hannah': 7, 'Nicole': 2, 'Donny': 2}, 8)
 get_top_editors_test2 = Function_Test( {'Bob':1, 'Hannah': 7, 'Nicole': 2, 'Donny': 2}, get_top_editors_actual_result2)
 get_top_editors_test2.__str__()
 if get_top_editors_test2.pass_or_fail == 'PASS':
 	successes +=1
 else:
 	fails += 1
 	
 	
 	
 print ('Now Testing Function: get_top_editors() ONE MORE TIME!')	
 get_top_editors_actual_result3 = get_top_editors ({'Dan':1, 'Vale': 7, 'Justin': 2, 'Ann': 3}, 2)
 get_top_editors_test3 = Function_Test( {'Vale': 7, 'Ann': 3}, get_top_editors_actual_result3)
 get_top_editors_test3.__str__()
 if get_top_editors_test3.pass_or_fail == 'PASS':
 	successes +=1
 else:
 	fails += 1
 
 
 print ('\n' 'Your Final test Results are:' '\n'
 				'Success = ', successes,
 				'Fails = ', fails)
main()
