'''Given 2 int values, return true if either of them is in the range 10..20 inclusive.'''

def in1020(a, b):
    return 10 <= a and a <= 20 or 10 <= b and b <= 20

''' codingbat test cases
12, 99, True
21, 12, True
8, 99, False
0, 0, False
0, 15, True
20, 0, True
10, 21, True
9, 21, False
9, 20, True
-10, -20, False
60000, 100000, False
-100000, -60000, False
'''

#difficulty:151