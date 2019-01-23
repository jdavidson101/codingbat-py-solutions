#Given 2 int values, return true if they are both in the range 30..40 inclusive, or they are both in the range 40..50 inclusive.

def in3050(a, b):
    return 30 <= a <= 40 and 30 <= b <= 40 or 40 <= a <= 50 and 40 <= b <= 50

''' codingbat test cases
30, 31, True
30, 41, False
40, 50, True
0, 0, False
0, 35, False
35, 0, False
30, 41, False
39, 41, False
40, 30, True
40, 50, True
60000, 100000, False
-100000, 60000, False
'''

#difficulty:175