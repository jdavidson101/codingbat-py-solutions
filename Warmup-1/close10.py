# Given 2 int values, return whichever value is nearest to the value 10, or return 0 in the event of a tie. 
# Note that abs(n) returns the absolute value of a number.

def close10(a, b):
    val1 = abs(10 - a)
    val2 = abs(10 - b)
    if val1 != val2:
        return a if val1 < val2 else b
    return 0
        