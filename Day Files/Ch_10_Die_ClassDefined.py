#  Chapter 10 Classes and OOP - from book coin flip.
#  Ch_10_Die_ClassDefined.py
# 6-sided die class simulator.
#          private variable value
#          Methods roll() - Physical rolling of 6-sided die (random.randint() )
#                  get_roll - returns roll value.


import random  # Get system random number for


class Die:     # Return uniform distribution of integers 1 through 6
    def __init__(self):
        self.value = 0       # initialize roll  integer type
    def roll(self):
        self.value= random.randint(1,6)
    def get_roll(self):
        return self.value
def main():
#        create an object from the Die class
    my_die = Die()       # object created
    print('Initial Value is    ', my_die.get_roll())
      # roll the object my_Die
    for i in range (10):
        my_die.roll()         # roll die.  
        print('Value after roll ',i+1, ' is ', my_die.get_roll())
# Call main function direct for class test.
if __name__=='__main__':
    main()


           
