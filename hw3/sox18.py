'''   
   Yu Lin
   CS5001 - Spring 2019
   HW3 (List and Loops)
   Feb 1, 2019 
'''

from baseball import calc_winners
from baseball import calc_losers
from baseball import calc_avg_runs
from baseball import calc_wins_losses

RECORD = ['L', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'L', 'W', 'W',
          'W', 'W', 'W', 'W', 'W', 'W', 'L', 'L', 'L', 'W', 'W', 'L', 'L',
          'W', 'W', 'L', 'W', 'L', 'W', 'W', 'W', 'L', 'L', 'W', 'L', 'W',
          'W', 'L', 'L', 'W', 'W', 'L', 'W', 'W', 'W', 'W', 'L', 'W', 'W',
          'L', 'W', 'W', 'W', 'L', 'L', 'W', 'W', 'W', 'W', 'L', 'L', 'W',
          'L', 'W', 'W', 'W', 'W', 'L', 'L', 'W', 'L', 'L', 'W', 'W', 'L',
          'W', 'W', 'W', 'W', 'L', 'W', 'L', 'W', 'W', 'W', 'W', 'W', 'W',
          'W', 'W', 'W', 'W', 'L', 'W', 'W', 'W', 'L', 'W', 'W', 'L', 'L',
          'W', 'W', 'W', 'W', 'L', 'W', 'W', 'W', 'W', 'W', 'W', 'L', 'W',
          'W', 'W', 'W', 'W', 'L', 'W', 'W', 'L', 'L', 'L', 'W', 'W', 'L',
          'L', 'L', 'W', 'W', 'W', 'L', 'W', 'L', 'W', 'W', 'W', 'L', 'L',
          'W', 'W', 'W', 'W', 'L', 'W', 'W', 'L', 'L', 'W', 'W', 'L', 'L',
          'W', 'W', 'L', 'L', 'L', 'W']

RUNS = [4, 1, 3, 2, 7, 4, 3, 10, 8, 14, 7, 6, 7, 10, 3, 10, 9, 8, 7, 0,
        1, 3, 4, 5, 3, 6, 4, 10, 6, 5, 5, 5, 6, 6, 2, 6, 5, 3, 5, 5, 5,
        3, 6, 6, 4, 6, 5, 4, 4, 3, 6, 8, 1, 8, 8, 6, 2, 3, 5, 9, 6, 7,
        2, 0, 4, 2, 2, 6, 5, 2, 6, 0, 9, 2, 1, 9, 14, 2, 5, 9, 9, 4, 1,
        11, 1, 4, 11, 3, 10, 15, 7, 5, 8, 4, 6, 7, 6, 5, 1, 0, 9, 5, 6,
        1, 4, 10, 3, 2, 1, 15, 4, 4, 5, 10, 10, 5, 19, 5, 6, 4, 2, 4, 7,
        5, 0, 4, 3, 10, 7, 3, 1, 1, 8, 14, 9, 1, 6, 0, 8, 5, 9, 3, 3, 6,
        7, 1, 4, 0, 5, 4, 2, 1, 11, 7, 4, 3, 6, 19, 3, 6, 5, 10]

def main():
	wins = calc_wins_losses (RECORD) [0]
	losses = calc_wins_losses (RECORD) [1]
	print ('In 2018 season, Red sox had', wins, 'wins and', losses, 'losses')
	print ('Average runs per game of the season is', calc_avg_runs (RUNS))
	print ('Games won with exactly 1 run =', calc_winners (RECORD, RUNS, 1))
	print ('Games lost with more than 6 runs =', calc_losers (RECORD, RUNS, 6))
	
main()
