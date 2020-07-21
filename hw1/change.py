
'''
    Yu Lin
    CS5001 - Spring 2019
    HW1 (data types and arithmetic operations)
    Jan 13, 2019


    Test Cases 

        Test case #1
        $7.264
        7 dollars, 1 quarters, 0 dimes, 0 nickles, 1 pennies

        Test case #2
        $15.475
        15 dollars, 1 quarters, 2 dimes, 0 nickles, 2 pennies

        Test case #3
        $2.6745
        2 dollars, 2 quarters, 1 dimes, 1 nickles, 2 pennies

        Test case #4
        $8.1948
        8 dollars, 0 quarters, 1 dimes, 1 nickles, 4 pennies
        
        Test case #5
        $0.9826
        0 dollars, 3 quarters, 2 dimes, 0 nickles, 3 pennies
'''



def main():



    # Declare my constants
    quart = 0.25
    dime = 0.1
    nickle = 0.05
    penny = 0.01

    # Prompt the user to enter change amount
    change = float(input('Enter the change amount \n'))

    # Breaking the the change amount into dollar value and coin value
    numDollar = change // 1
    print (numDollar)
    coinVal = float ('.' + str(change).split('.') [1]) 
    print (coinVal)

    # Calculate the number of each coin type
    numQuart = coinVal // quart
    remainder = coinVal - (quart * numQuart)
    print (remainder)
    numDime = remainder // dime
    remainder = remainder - (dime * numDime)
    print (remainder)
    numNickle = remainder // nickle
    remainder = remainder - (nickle * numNickle)
    print (remainder)
    numPenny = remainder // penny


    # Output change
    print ('That breaks down to... \n',
           int(numDollar), 'dollars \n',
           int(numQuart),  'quarters \n',
           int(numDime),    'dimes \n',
           int(numNickle), 'nickles \n',
           int(numPenny),  'pennies \n' )



main()


