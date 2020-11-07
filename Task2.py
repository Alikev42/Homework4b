#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
# 
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Homework 3, part 4.2
    Create a function that randomly generates and returns a tuple of two positive 
one-digit integers. Then prompt the user for the multiplication of the two numbers. 
For example, if the generated number is 3 and 7, the prompt message is 
How much is 3 times 7? 
    Then compare the user answer with the correct result. If the answer is correct, 
display a message “done”. Otherwise, if the user input 20, prompt:
“3 times 7 is not 20, please try again: “
    Keep asking the user input until it types the correct answer.
    
"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules
import random

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables
GlobalTuple = (0,0) # Explicit global creation of a tuple, with dummy values
MultValue = 0       # Integer 
UserProd = 0        # Integer
Correct = 0         # Boolean Integer, 0 = false, 1 = true

#########1#########2#########3#########4#########5#########6#########7#########8
# Functions
def GenRandTuple():
    LocalTuple = (0,0)  # Explicit local creation of a tuple, with dummy values
    
    LocalTuple = (random.randint(0,9), random.randint(0,9))
    return LocalTuple
#--------1---------2---------3---------4---------5---------6---------7---------8#
#########1#########2#########3#########4#########5#########6#########7#########8
# Main
GlobalTuple = GenRandTuple()
MultValue = GlobalTuple[0] * GlobalTuple[1]

while Correct == 0:
    UserStr = input(f'What is the product of {GlobalTuple[0]} and {GlobalTuple[1]}?')
    UserProd = int(UserStr)

    if UserProd == MultValue:
        Correct = 1
    else:
        print(f'{GlobalTuple[0]} times {GlobalTuple[1]} is not {UserProd}.  Please try again. ')

print('Done')
# End Main
#########1#########2#########3#########4#########5#########6#########7#########8