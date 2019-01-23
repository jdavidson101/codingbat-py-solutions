'''We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, return true if 1 or more of them are teen.'''

def has_teen(a, b, c):
    return a >= 13 and a <= 19 or b >= 13 and b <= 19 or c >= 13 and c <= 19

''' coding bat test cases
13, 20, 10, True
20, 19, 10, True
0, 0, 0, False
15, 0, 0, True
0, 15, 0, True
0, 0, 15, True
12, 20, 0, False
9, -21, -14, False
10, 13, 30, True
12, 34, 19, True
15, 13, 18, True
'''

#difficulty:154