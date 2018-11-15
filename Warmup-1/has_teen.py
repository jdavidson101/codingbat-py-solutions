'''We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, return true if 1 or more of them are teen.'''

def has_teen(a, b, c):
    return a >= 13 and a <= 19 or b >= 13 and b <= 19 or c >= 13 and c <= 19