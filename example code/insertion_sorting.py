''' CS5001 
    Spring 2019
    Lab 10 -- insertion sort
    Sample Solution 
'''

def insertion_sort(lst):
		
	for i in range(1, len(lst)):
		
		j = i - 1
		a = lst[i]
		while a < lst[j] and j>=0:
			lst[j+1] = lst [j]
			j = j - 1
		lst [j+1] = a
		

	return lst
	
	
def main():
	lst = [5,1,2]
	print(insertion_sort(lst))
			
	
	
	
	
	
	
main()
