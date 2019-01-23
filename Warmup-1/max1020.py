# Given 2 positive int values, return the larger value that is in the range 10..20 inclusive, or return 0 if neither is in that range.

def max1020(a, b):
    range_a = a >= 10 and a <= 20
    range_b = b >= 10 and b <= 20
    if range_a or range_b:
        if range_a and range_b:
            return a if a > b else b
        return a if range_a else b
    return 0

''' codingbat test cases
11, 19, 19
10, 21, 10
9, 21, 0
0, 0, 0
0, 15, 15
15, 0, 15
20, 0, 20
9, 20, 20
17, 24, 17
60000, 14, 14
21, 60000, 0
17, 19, 19
19, 17, 19
'''

#difficulty:178