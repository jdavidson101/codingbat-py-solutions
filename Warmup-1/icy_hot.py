'''Given two temperatures, return true if one is less than 0 and the other is greater than 100.'''

def icy_hot(temp1, temp2):
    return temp1 > 100 and temp2 < 0 or temp1 < 0 and temp2 > 100

''' codingbat test cases
120, -1, True
-1, 120, True
2, 120, False
0, 0, False
0, 100, False
-1, 100, False
100, -1, False
-1, 101, True
101, -1, True
101, 0, False
60000, -1, True
101, -60000, True
'''

#difficulty:148