'''Given two temperatures, return true if one is less than 0 and the other is greater than 100.'''

def icy_hot(temp1, temp2):
    if temp1 > 100 and temp2 < 0 or temp1 < 0 and temp2 > 100:
        return True
    return False