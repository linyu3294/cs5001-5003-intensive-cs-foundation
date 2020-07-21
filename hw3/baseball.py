'''   
   Yu Lin
   CS5001 - Spring 2019
   HW3 (List and Loops)
   Feb 1, 2019 
   
   Contains Functions that will be used in sox18.py
'''

def calc_wins_losses(record_list): 
	''' 
			Function: calc_wins_losses
			Input: a list (a record of wins/losses from a season)
			Returns: a list with two values, total wins and total losses
	'''
	wins = 0
	losses = 0
	for i in range(len(record_list)):
		if record_list[i].upper() == 'W':
			wins += 1
		elif record_list[i].upper() == 'L':
			losses += 1
	return [wins, losses]


def calc_avg_runs(runs_list):
	''' 
			Function: calc_avg_runs
			Input: a list (a record of runs from a season)
			Returns: a float rounded to the second place, which represents the average   runs per game during a season
	'''
	total_runs = 0
	total_games = len(runs_list)
	for i in range(total_games):
		total_runs = total_runs + runs_list[i]
		avg_runs = total_runs / total_games
	return '{:0.2f}'.format(avg_runs)
	
	
def calc_winners(record_list, run_list, runs):
	''' 
			Function: calc_winners
			Input: a list (a record of wins/losses from a season), a list (a record of runs from a season), and a int (number of runs in a game)
			Returns: a int, which represents number of games that were won and that also have the specified number of runs passed as an input of the function
	'''
	winners = 0
	for i in range(len(record_list)):
		if record_list[i].upper() == 'W' and run_list[i] == runs:
			 winners += 1
	return winners 
	
	
def calc_losers(record_list, run_list, runs):
	''' 
			Function: calc_losers
			Input: a list (a record of wins/losses from a season), a list (a record of runs from a season), and a int (number of runs in a game)
			Returns: a int, which represents number of games that were lost and that also have the specified number of runs passed as an input of the function
	'''
	losers = 0
	for i in range(len(record_list)):
		if record_list[i].upper() == "L" and run_list[i] >= runs:
			losers += 1
	return losers
	


