'''We'll say that a number is "teen" if it is in the range 13..19 inclusive. 
Given 2 int values, return true if one or the other is teen, but not both.'''

def lone_teen(a, b):
    if a >= 13 and a <= 19 and (b < 13 or b > 19): return True
    if b >= 13 and b <= 19 and (a < 13 or a > 19): return True
    return False

''' codingbat test cases
13, 99, True
21, 19, True
13, 13, False
0, 0, False
15, 0, True
0, 15, True
12, 20, False
9, -21, False
10, 13, True
19, 34, True
24, 14, True
14, 24, True
15, 13, False
'''

#difficulty:157