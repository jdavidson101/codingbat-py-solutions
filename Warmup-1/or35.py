'''Return true if the given non-negative number is a multiple of 3 or a multiple of 5. Use the % "mod" operator -- see Introduction to Mod'''

def or35(n):
    return n != 0 and (n % 3 == 0 or n % 5 == 0)

''' codingbat test cases
3, True
10, True
8, False
0, False
2, False
5, True
9, True
80000, True
11, False
2147483647, False
'''

#difficulty:140