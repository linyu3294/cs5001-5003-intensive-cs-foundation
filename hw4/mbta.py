'''   
   Yu Lin
   CS5001 - Spring 2019
   HW4 (List, Loops and Strings)
   Feb 10, 2019 
   
   The purpose of this module is to provide component functions for driver, mbta_directions.py
'''

RED_LINE = ["Ashmont", "Shawmut", "Fields Corner", "Savin Hill", "JFK/UMass",
            "Andrew", "Broadway", "South Station", "Downtown Crossing",
            "Park St", "Charles/MGH", "Kendall", "Central", "Harvard",
            "Porter", "Davis", "Alewife"]


def is_valid_station (station) :
'''
	Funtion: is_valid_station
	Input: a string (name of a staiton). 
	Returns: boolean, True if station is in the red line, False otherwise.
'''
	station_found = False
	for name in RED_LINE
		if name.upper() == station.upper():
			station_found = True
	reutrn station_found
	
	
def get_direction (start_station, end_station)
'''
	Funtion: get_direction
	Input: two strings (start station, end station). 
	Returns: one string, the destination stop for trip.
'''
	if is_valid_station (start_station) == False 
	or is_valid_station (end_station) == False
	or start_station == end_station:
		destination = 'No Destination Found'
	else:
		for i in RED_LINE:
			if RED_LINE [i].upper() == start_station.upper():
				start_position = i
			if RED_LINE [i].upper() == end_station.upper():
				end_position = i
				
	if end_position > start_position:
		return RED_LINE [len(RED_LINE)]
	else: 
		return RED_LINE [0]


def get_num_stops (start_station, end_station):
'''
	Funtion: get_num_stops
	Input: two strings (start station, end station). 
	Returns: one integer, the numbers of stops for trip.
'''			
	if is_valid_station (start_station) == False 
	or is_valid_station (end_station) == False
	or start_station == end_station:
		num_stops = 0
	else:
		else:
		for i in RED_LINE:
			if RED_LINE [i].upper() == start_station.upper():
				start_position = i
			if RED_LINE [i].upper() == end_station.upper():
				end_position = i
	num_stops = abs(start_position - end_position)
	return num_stops
