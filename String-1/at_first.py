'''Given a string, return a string length 2 made of its first 2 chars. 
If the string length is less than 2, use '@' for the missing chars.'''

def at_first(str):
    if len(str) < 2: str += '@' * (2 - len(str))
    return str[:2]