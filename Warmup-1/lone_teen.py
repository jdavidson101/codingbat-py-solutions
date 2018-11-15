'''We'll say that a number is "teen" if it is in the range 13..19 inclusive. 
Given 2 int values, return true if one or the other is teen, but not both.'''

def lone_teen(a, b):
    if a >= 13 and a <= 19 and (b < 13 or b > 19): return True
    if b >= 13 and b <= 19 and (a < 13 or a > 19): return True
    return False