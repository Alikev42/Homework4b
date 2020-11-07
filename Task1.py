#########1#########2#########3#########4#########5#########6#########7#########8
# Kevin R. Salger
# IS 640 Business Application Programming (Python)
#
#########1#########2#########3#########4#########5#########6#########7#########8
#        11111111112222222222333333333344444444445555555555666666666677777777778
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#########1#########2#########3#########4#########5#########6#########7#########8
"""
Homework 3, part 4.1
    A prime number is a number that is only evenly divisible by itself and 1.  
For example, the number 5 is prime because it can only be evenly divided by 1 and 5.  
The number 6, however, is not prime because it can be divided evenly by 2 and 3.
    Write a Boolean function named is_prime which takes an integer as an argument
and returns true if the argument is a prime number, or false otherwise. 
    Then write a program that generates six random number between 1 and 100 (inclusive) 
and print out the result like the following (each run will have six different random numbers):
The random number 87 is a not a prime number.
The random number 23 is a prime number.
The random number 34 is a not a prime number.
The random number 96 is a not prime number.
The random number 6 is a not a prime number.
The random number 11 is a prime number.

"""
#########1#########2#########3#########4#########5#########6#########7#########8
# Imported Modules
import random

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Constants

#########1#########2#########3#########4#########5#########6#########7#########8
# Global Variables
i = 0   # Integer Counting variable
UserNum = [0, 0, 0, 0, 0, 0] # Integer List, six members, dummy values
PrimeList = [0, 0, 0, 0, 0, 0] # Integer List, six members, dummy values

#########1#########2#########3#########4#########5#########6#########7#########8
# Function(s)
#--------1---------2---------3---------4---------5---------6---------7---------8#
def is_prime(TestNum):
    # Local assignments
    PrimeYN = 0 # Assignment 0 to PrimeYN.  0 = False, 1 = True

    if ((TestNum % 2 == 0) or 
        (TestNum % 3 == 0) or 
        (TestNum % 5 == 0) or 
        (TestNum % 7 == 0)):
        PrimeYN = 0
    else:
        PrimeYN = 1
    return PrimeYN
        
    # End is_prime()
#--------1---------2---------3---------4---------5---------6---------7---------8#
#########1#########2#########3#########4#########5#########6#########7#########8
# Main
#   Generate six random numbers & assign to list UserNum
for i in range(0,6,1):
    UserNum[i] = random.randint(0,100)

# Check each number for primeness
for i in range (0,6,1):
    PrimeList[i] = is_prime(UserNum[i])

# Print the results
for i in range (0,6,1):
    if PrimeList[i] == 1:
        print(f'The random number {UserNum[i]} is a prime number.')
    elif PrimeList[i] == 0:
        print(f'The random number {UserNum[i]} is not a prime number.')
# End Main
#########1#########2#########3#########4#########5#########6#########7#########8