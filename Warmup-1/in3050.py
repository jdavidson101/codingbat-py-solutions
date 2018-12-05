#Given 2 int values, return true if they are both in the range 30..40 inclusive, or they are both in the range 40..50 inclusive.

def in3050(a, b):
    return 30 <= a <= 40 and 30 <= b <= 40 or 40 <= a <= 50 and 40 <= b <= 50