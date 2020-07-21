'''
	CS 5001
	Spring 2019
	Class Object - Demo
	__str__ and __eq__ def examples
'''

class Car:
    def __init__(self, make = 'Powell', model = 'The Homer'):
        self.make = make
        self.model = model
        self.year = 1991
        self.price = 82000.0

    def __str__(self):
        printable = 'The ' + self.make + ' ' + self.model + '\n' \
                    + 'Year: ' + str(self.year) + '\n' \
                    + 'It costs you: $' + '{:.2f}'.format(self.price)
        return printable

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model
