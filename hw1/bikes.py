'''
    Yu Lin
    CS5001 - Spring 2019
    HW1 (data types and arithmetic operations)
    Jan 13, 2019


    Test Cases

        Test case #1
        176 wheels, 7 frames, 289 links
        5 bikes, w/leftover (166 wheels, 2 frames, 39 links)

        Test case #2
        7 wheels, 5200 frames, 500 links
        3 bikes, w/leftover (1 wheels, 5197 frames, 350 links)

        Test case #3
        31 wheels, 20 frames, 49 links
        0 bikes, w/leftover (31 wheels, 20 frames, 49 links)

        Test case #4
        48 wheels, 4 frames, 265 links
        4 bikes, w/leftover (40 wheels, 0 frames, 65 links)

        Test case #5
        4 wheels, 2 frames, 100 links
        2 bikes, w/leftover (0 wheels, 0 frames, 0 links)

'''



def main():


  # Prompt the user to enter number of wheels
  numWheels = float(input('Enter the number of wheels \n'))
  # Prompt the user to enter number of frames
  numFrames = float(input('Enter the number of frames \n'))
  # Prompt the user to enter number of 
  numLinks = float(input('Enter the number of links \n'))

  # calculate total bikes can be made from parts
  numBikes = min (int (numWheels // 2),
                  int (numFrames // 1),
                  int (numLinks // 50))

  # Out put total bikes and leftovers
  loWheels = int(numWheels - (numBikes * 2))
  loFrames = int(numFrames - (numBikes))
  loLinks = int(numLinks - (numBikes * 50))

  print ('All totalled up, you\'ve got', numBikes,'bikes coming \n',
         'I\'m keeping the lefovers for myself \n',
         'Leftovers: \n',
         loWheels, 'wheels \n',
         loFrames, 'frames \n',
         loLinks, 'links \n') 




main()
