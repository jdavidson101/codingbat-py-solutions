# Given two non-negative int values, return true if they have the same last digit, such as with 27 and 57. 
# Note that the % "mod" operator computes remainders, so 17 % 10 is 7.

def last_digit(a, b):
    return a % 10 == b % 10

''' codingbat test cases
7, 17, True
6, 17, False
3, 113, True
0, 0, True
0, 15, False
15, 0, False
20, 0, True
6, 86, True
51, 9, False
81238791989, 1239898239, True
'''

#difficulty:184